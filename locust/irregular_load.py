from locust import LoadTestShape
import math

class IrregularLoadShape(LoadTestShape):
    duration = 3600
    users = [
        10, 90, 24, 75, 38, 99, 14,
        46, 62, 23, 71, 12, 76, 53,
        19, 94, 64, 72, 23, 86, 16,
        85, 34, 26, 23, 95, 12, 43,
        90, 54, 23, 81, 45, 23, 91,
        74, 29, 56, 74, 100, 8, 34
    ]

    def tick(self):
        run_time = self.get_run_time()
        current_users = self.get_current_user_count()

        if run_time >= self.duration:
            return None

        index = math.floor(run_time/self.duration * len(self.users))
        return (self.users[index], self.users[index])
