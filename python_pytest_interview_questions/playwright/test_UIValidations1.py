import time


from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions")
    page.get_by_role("button", name="Sign In").click()

    # case is select 2 items iphone x and nokia edge, -> and them in cart
    # and verify the items are showing in cart

    iPhoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iPhoneProduct.get_by_role("button").click()

    nokiaEdge = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaEdge.get_by_role("button").click()

    page.get_by_text(("Checkout")).click()

    # check count
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(5)

# this testcase demonstrates the new open tab
def test_childWindowHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # new child page will always be written in the closure
    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").filter(has_text="Free Access to InterviewQues/ResumeAssistance/Material").click()
        # page.locator(".blinkingText[href='https://rahulshettyacademy.com/documents-request']").click()
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        print(text)  #Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words = text.split("at") #0-> Please email us at  #1-> mentor@rahulshettyacademy.com with below template to receive response
        email = words[1].strip().split(" ")[0] #to remove the space we are using strip()
        assert email == "mentor@rahulshettyacademy.com"


# check the price of rice is equal to 37$
def test_tableAutomation(page: Page):
    global colPriceValue
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    # identify the price column and rice column and the moment you get both extract both the values
    # iterate each locator through forloop to find the text called price
    for i in range(page.locator("th").count()):
        if page.locator("th").nth(i).filter(has_text="Price").count() > 0:
            colPriceValue = i
            print(f"Price column value is {colPriceValue}")
            break
    riceRow = page.locator("tr").filter(has_text="Rice")
    print(riceRow)
    expect(riceRow.locator("td").nth(colPriceValue)).to_have_text("37")

# Mouse hover
def test_MouseHover(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()