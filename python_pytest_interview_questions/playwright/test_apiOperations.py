"""
Login from ui
Place order from postman
Grab order id from api response through playwright
Switch back to ui and from orders tab, find the order id that matches order response, confirming order placed successfully.
Go to view and ensure the delivery address information from order summary
"""
import time

from playwright.sync_api import Page, Playwright, expect

from utils.apiBase import APIUtils


def test_order_details(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    #first create order
    apiUtils = APIUtils()
    orderId = apiUtils.createOrder(playwright)

    #then go to login page
    page.locator("#userEmail").fill("rutushah105@gmail.com")
    page.locator("#userPassword").fill("Rutu@123")
    page.get_by_role("button",name="Login").click()
    time.sleep(5)

    #orders History page -> confirm order is present
    page.get_by_role("button",name="ORDERS").click()
    orderCreatedRow = page.locator("tr").filter(has_text=orderId)
    orderCreatedRow.get_by_role("button",name="View").click()
    expect(page.locator(".col-text")).to_contain_text(orderId)
    context.close()
    
