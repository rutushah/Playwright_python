from playwright.sync_api import expect

from .ordersDetailPage import OrderDetailsPage


class OrdersHistoryPage:

    def __init__(self, page):
        self.page = page

    def selectOrder(self, orderId):
        orderCreatedRow = self.page.locator("tr").filter(has_text=orderId)
        orderCreatedRow.get_by_role("button", name="View").click()
        orderDetails = OrderDetailsPage(self.page)
        return orderDetails