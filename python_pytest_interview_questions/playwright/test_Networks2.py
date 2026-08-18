# import route
import time
from email import message

from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils

"""
intercepting response this time
api call goes from the browser that is contacting the server
"""
def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/client/#/dashboard/order-details/6a7f951521054ba463442")

def test_Network1(page:Playwright):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)

    #then go to login page
    page.locator("#userEmail").fill("rutushah105@gmail.com")
    page.locator("#userPassword").fill("Rutu@123")
    page.get_by_role("button",name="Login").click()


    # orders History page -> confirm order is present
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button",name="View").first.click()
    time.sleep(5)

    validate = page.locator(".blink_me").text_content()
    print(validate)
    expect(validate).to_contain_text("You are not authorize to view this order")

def test_sessionStorage(playwright:Playwright):
    apiUtils = APIUtils()
    getToken = apiUtils.getToken(playwright)
    browser= playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # script to inject token in session local storage
    # any javascript injection has to be in triple quotes
    page.add_init_script(f"""localStorage.setItem('token','{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client/")

    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()