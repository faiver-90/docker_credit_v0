# import os
#
# from dotenv import load_dotenv
# from locust import HttpUser, TaskSet, task, between
#
# from credit_v0.tests.playwright.test_pw import DOMAIN
#
# load_dotenv()
# PASS_ALL_ACC = os.getenv("PASS_ALL_ACC")
#
#
# class UserBehavior(TaskSet):
#     def on_start(self):
#         """This method is called when a Locust user starts before any task is scheduled"""
#         self.login()
#
#     def login(self):
#         self.client.post("/credit/login/", data={"username": "test_user", "password": f"{PASS_ALL_ACC}"})
#
#     @task(1)
#     def index(self):
#         self.client.get("/credit/car-form/118/")
#
#
# class WebsiteUser(HttpUser):
#     tasks = [UserBehavior]
#     wait_time = between(1, 10)
#     host = f"https://{DOMAIN}"
