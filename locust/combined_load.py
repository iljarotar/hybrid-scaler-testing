from locust import LoadTestShape
import math

class CombinedLoadShape(LoadTestShape):
    irregular_load_duration = 1200
    high_load_duration = 1200
    steady_load_duration = 1200
    duration = irregular_load_duration + high_load_duration + steady_load_duration

    high_load_spawn_rate = 0.3
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

        checkpoint = self.irregular_load_duration

        if (run_time - checkpoint) <= self.high_load_duration:
            if (run_time - checkpoint) <= self.high_load_duration / 2:
                users = math.floor((run_time - checkpoint) * self.high_load_spawn_rate)
                return (min(users, self.high_load_users), self.high_load_spawn_rate)

            remaining_time = self.high_load_duration - (run_time - checkpoint)
            users = math.floor(remaining_time * self.high_load_spawn_rate)
            return (min(users, self.high_load_users), self.high_load_spawn_rate)

        checkpoint = self.irregular_load_duration + self.high_load_duration
        
        if (run_time - checkpoint) <= self.steady_load_duration / 2:
            users = math.floor((run_time - checkpoint) * self.steady_load_spawn_rate)
            return (min(users, self.steady_load_users), self.steady_load_spawn_rate)

        remaining_time = self.duration - run_time
        users = math.floor(remaining_time * self.steady_load_spawn_rate)
        return (min(users, self.steady_load_users), self.steady_load_spawn_rate)
