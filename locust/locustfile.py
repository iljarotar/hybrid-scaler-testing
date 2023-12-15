from locust import HttpUser, task, between, constant_pacing, constant

# makes light requests at a steady pace
class LightSteadyUser(HttpUser):
    weight = 4
    wait_time = constant_pacing(1)

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
    def twelve_ten(self):
        self.client.get("/?range=12&notes=10")

    @task
    def twelve_eleven(self):
        self.client.get("/?range=12&notes=11")

    @task
    def twelve_twelve(self):
        self.client.get("/?range=12&notes=12")

# makes medium and heavy requests with short pauses in between
class HeavyUser(HttpUser):
    weight = 1
    wait_time = between(1, 15)

    @task
    def sixteen_twelve(self):
        self.client.get("/?range=16&notes=12")

    @task
    def sixteen_five(self):
        self.client.get("/?range=16&notes=5")

# makes light requests often and heavy requests sometimes
class MixedUser(HttpUser):
    weight = 2
    wait_time = constant(1)

    @task
    def sixteen_nine(self):
        self.client.get("/?range=16&notes=9")

    @task(5)
    def twelve_seven(self):
        self.client.get("/?range=12&notes=7")

    @task(5)
    def twelve_four(self):
        self.client.get("/?range=12&notes=4")

    @task
    def twelve_five(self):
        self.client.get("/?range=12&notes=5")

    @task
    def twelve_six(self):
        self.client.get("/?range=12&notes=6")

    @task
    def twelve_eight(self):
        self.client.get("/?range=12&notes=8")

    @task
    def twelve_nine(self):
        self.client.get("/?range=12&notes=9")

# makes mixed requests very sporadically
class IrregularUser(HttpUser):
    weight = 2
    wait_time = between(2, 30)

    @task
    def sixteen_thirteen(self):
        self.client.get("/?range=16&notes=13")

    @task
    def sixteen_four(self):
        self.client.get("/?range=16&notes=4")  

    @task
    def thirteen_seven(self):
        self.client.get("?range=13&notes=7")

    @task
    def fifteen_five(self):
        self.client.get("/?range=15&notes=5")
