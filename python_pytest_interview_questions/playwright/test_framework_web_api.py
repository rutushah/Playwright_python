import json

import pytest

from conftest import browserInstance
from pageObjects.login import LoginPage
import time

from playwright.sync_api import Page, Playwright, expect

from utils.apiFrameworkBase import APIUtils
"""
To drive test data from external source like excel, json, etc
These days most of the industry is using data from json file to drive test data.

Steps to implement
1. Create a json file with test data
2. Create a util, that converts json data into python list or dictionary
"""


# accessing json file
with open('data/credentials.json') as json_file:
    test_data = json.load(json_file)
    print(test_data)
    user_credentials_list = test_data['user_credentials']
@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials',user_credentials_list)
def test_order_details(playwright: Playwright,browserInstance,user_credentials):
    userEmail = user_credentials['userEmail']
    userPassword = user_credentials['password']

    #first create order
    apiUtils = APIUtils()
    orderId = apiUtils.createOrder(playwright,user_credentials)

    # object for login page class
    loginPage = LoginPage(browserInstance)
    #then go to login page
    loginPage.navigate()
    dashboardPage = loginPage.login(userEmail, userPassword)

    # dashboardPAge

    ordersHistoryPage = dashboardPage.selectOrdersNavLink()
    orderDetails = ordersHistoryPage.selectOrder(orderId)
    orderDetails.verifyOrderMessage(orderId)
