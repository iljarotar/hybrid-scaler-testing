from locust import LoadTestShape
import random

class IrregularLoadShape(LoadTestShape):
    duration = 3600
    max_users = 100

    def tick(self):
        run_time = self.get_run_time()
        current_users = self.get_current_user_count()

        if run_time >= self.duration:
            return None

        if run_time % 100 < 1:
            users = random.randint(0, self.max_users)
            return (users, users)

        return (current_users, 1)
