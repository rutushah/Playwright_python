from playwright.sync_api import Page, Playwright, expect

from pageObjects import ordersHistoryPage
from .ordersHistoryPage import OrdersHistoryPage

class DashboardPage:

    def __init__(self,page):
        self.page = page

    def selectOrdersNavLink(self):
         #orders History page -> confirm order is present
         self.page.get_by_role("button",name="ORDERS").click()
         orderHistory = OrdersHistoryPage(self.page)
         return orderHistory
