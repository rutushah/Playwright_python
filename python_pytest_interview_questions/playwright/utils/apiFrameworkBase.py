from playwright.sync_api import Playwright

from conftest import user_credentials


ordersPayload = {"orders": [{"country": "United States", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}


class APIUtils:
    def getToken(self, playwright: Playwright,user_credentials):
        userEmail = user_credentials['userEmail']
        userPassword = user_credentials['password']
        loginPayload = {"userEmail": userEmail, "userPassword": userPassword}
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/auth/login",
                                 data=loginPayload,
                                 headers={
                                     "Content-Type": "application/json"
                                 })
        # check response is 200 ok
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]


    def createOrder(self, playwright: Playwright,user_credentials):
        token = self.getToken(playwright,user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data=ordersPayload,
                                            headers={"Authorization": token,
                                                     "Content-Type": "application/json"
                                                     })
        print(response.json())
        responseBody = response.json()
        orderId  =  responseBody["orders"][0]
        return orderId