from locust import HttpUser, task, between


data = {'user_1': 1, 'user_2': 2}


class Test(HttpUser):
    wait_time = between(0.2, 0.3)

    @task
    def send(self):
        self.client.post('/task/', json=data)