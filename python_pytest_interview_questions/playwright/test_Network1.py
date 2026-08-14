# import route
from playwright.sync_api import Playwright
"""
 make api call from browser ->
  api call contact server and return backs response
  browser use response to generate the data
"""
fakePayloadOrderResponse = {"data": [], "message": "No Orders"}

def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

def test_Network1(page:Playwright):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_response)

    #then go to login page
    page.locator("#userEmail").fill("rutushah105@gmail.com")
    page.locator("#userPassword").fill("Rutu@123")
    page.get_by_role("button",name="Login").click()

    # orders History page -> confirm order is present
    page.get_by_role("button", name="ORDERS").click()

    #scenario here is to validate when there are no orders you will see "No orders present message"
    # this can be achieved without deleting test data or creating new user , simply by just mocking the test data
    no_orders_text = page.locator(".mt-4").text_content()
    print(no_orders_text)