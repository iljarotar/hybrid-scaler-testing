from locust import HttpUser, task, between, constant_pacing, constant

class User(HttpUser):
    wait_time = between(0.5,15)

    @task
    def twelve_one(self):
        self.client.get("/?range=12&notes=1")

    @task
    def twelve_two(self):
        self.client.get("/?range=12&notes=2")

    @task
    def twelve_three(self):
        self.client.get("/?range=12&notes=3")

    @task
    def twelve_four(self):
        self.client.get("/?range=12&notes=4")

    @task
    def twelve_five(self):
        self.client.get("/?range=12&notes=5")

    @task
    def twelve_six(self):
        self.client.get("/?range=12&notes=6")

    @task
    def twelve_seven(self):
        self.client.get("/?range=12&notes=7")

    @task
    def twelve_eight(self):
        self.client.get("/?range=12&notes=8")

    @task
    def twelve_nine(self):
        self.client.get("/?range=12&notes=9")

    @task
    def twelve_ten(self):
        self.client.get("/?range=12&notes=10")

    @task
    def twelve_eleven(self):
        self.client.get("/?range=12&notes=11")

    @task
    def twelve_twelve(self):
        self.client.get("/?range=12&notes=12")
