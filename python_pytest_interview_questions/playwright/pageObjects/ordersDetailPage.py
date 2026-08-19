from playwright.sync_api import expect


class OrderDetailsPage:
    def __init__(self, page):
        self.page = page

    def verifyOrderMessage(self,orderId):
        expect(self.page.locator(".col-text")).to_contain_text(orderId)