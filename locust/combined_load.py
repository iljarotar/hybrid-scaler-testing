from locust import LoadTestShape
import math

class CombinedLoadShape(LoadTestShape):
    irregular_load_duration = 3600
    high_load_duration = 3600
    steady_load_duration = 3600
    duration = irregular_load_duration + high_load_duration + steady_load_duration

    high_load_spawn_rate = 2
    high_load_users = 1000
    steady_load_spawn_rate = 1
    steady_load_users = 600

    irregular_users_numbers = [
        150, 24, 912, 765, 99, 1,
    ]

    def tick(self):
        run_time = self.get_run_time()

        if run_time >= self.duration:
            return None

        if run_time <= self.irregular_load_duration:
            index = math.floor(run_time/self.irregular_load_duration * len(self.irregular_users_numbers))
            return (self.irregular_users_numbers[index], self.irregular_users_numbers[index])

        high_load_run_time = run_time - self.irregular_load_duration

        if high_load_run_time <= self.high_load_duration:
            if high_load_run_time <= self.high_load_duration / 2:
                users = math.floor(high_load_run_time * self.high_load_spawn_rate)
                return (min(users, self.high_load_users), self.high_load_spawn_rate)

            remaining_time = self.high_load_duration - high_load_run_time
            users = math.floor(remaining_time * self.high_load_spawn_rate)
            return (min(users, self.high_load_users), self.high_load_spawn_rate)

        steady_load_run_time = run_time - (self.irregular_load_duration + self.high_load_duration)
        
        if steady_load_run_time <= self.steady_load_duration / 2:
            users = math.floor(steady_load_run_time * self.steady_load_spawn_rate)
            return (min(users, self.steady_load_users), self.steady_load_spawn_rate)

        remaining_time = self.duration - run_time
        users = math.floor(remaining_time * self.steady_load_spawn_rate)
        return (min(users, self.steady_load_users), self.steady_load_spawn_rate)
