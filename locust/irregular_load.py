from locust import LoadTestShape

class IrregularLoadShape(LoadTestShape):
    duration = 3600
    users = 50

    def tick(self):
        run_time = self.get_run_time()
        current_users = self.get_current_user_count()

        if run_time >= self.duration:
            return None

        if current_users < self.users:
            return (self.users, self.users)

        return (self.users, current_users)
