import time

from playwright.sync_api import Page, expect, playwright

def test_playwrightBasics(playwright):
    # invoking browser object
    browser = playwright.chromium.launch(headless=False)
    # opening browser in new context like incognito etc
    context = browser.new_context()
    # to open new page we use context.new_page() method
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")

# page fixture have implemented chromium browser launch in headless mode in 1 single context
def test_playwrightShortCut(page: Page):
    page.goto("https://rahulshettyacademy.com/")

def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # identify the input box using label method
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@sesettrx")
    # important locator called get_by_role() -> to identify role base  component of the page
    # here in the combo box of select option, option value should be passed
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link",name="terms and conditions")
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)


def test_firefoxBrowser(playwright):
    firefoxBrowser = playwright.firefox
    browser = firefoxBrowser.launch(headless=False)
    page = browser.new_context()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # identify the input box using label method
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@sesettrx")
    # important locator called get_by_role() -> to identify role base  component of the page
    # here in the combo box of select option, option value should be passed
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)