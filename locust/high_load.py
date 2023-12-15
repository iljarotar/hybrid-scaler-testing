from locust import LoadTestShape
import math

class HighLoadShape(LoadTestShape):
    duration = 2400
    users = 80
    spawn_rate = 0.1

    def tick(self):
        run_time = self.get_run_time()

        if run_time >= self.duration:
            return None

        if run_time < self.duration / 2:
            users = math.floor(run_time * self.spawn_rate)
            return (min(users, self.users), self.spawn_rate)

        if run_time > self.duration / 2:
            remaining_time = self.duration - run_time
            users = math.floor(remaining_time * self.spawn_rate)
            return (min(users, self.users), self.spawn_rate)
