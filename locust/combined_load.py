from locust import LoadTestShape
import math

class CombinedLoadShape(LoadTestShape):
    irregular_load_duration = 1200
    high_load_duration = 600
    steady_load_duration = 400
    duration = irregular_load_duration + high_load_duration + steady_load_duration

    high_load_spawn_rate = 0.7
    high_load_users = 300
    steady_load_spawn_rate = 0.5
    steady_load_users = 100

    irregular_users_numbers = [
        10, 90, 24, 75, 38, 99, 14,
        46, 62, 23, 71, 12, 76, 53,
        19, 94, 64, 72, 23, 86, 16,
        85, 34, 26, 23, 95, 12, 43,
        90, 54, 23, 81, 45, 23, 91,
        74, 29, 56, 74, 100, 8, 34
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
