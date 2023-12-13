from locust import HttpUser, task

class User(HttpUser):
    @task
    def request(self):
        self.client.get("/?range=12&notes=7")
