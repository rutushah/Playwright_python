import time

from .dashboard import DashboardPage


class LoginPage:

    def __init__(self,page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    def login(self, userEmail, userPassword):
        self.page.locator("#userEmail").fill(userEmail)
        self.page.locator("#userPassword").fill(userPassword)
        self.page.get_by_role("button", name="Login").click()
        time.sleep(5)
        dashboardPage = DashboardPage(self.page)
        return dashboardPage


