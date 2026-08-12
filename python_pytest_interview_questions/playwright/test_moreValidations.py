import time
from tkinter import dialog

from playwright.sync_api import Page, expect


# to check use of get by placeholder, visible and hidden
def test_moreUIValidations(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

# alertboxes
def test_alerts(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # tell chance of triggering alert
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button",name="Confirm").click()
    time.sleep(4)

'''
Frames -> are nothing but another html page embedded in your parent html 
page, but not part of parent html page

'''

def test_frameHandling(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
#   for frames we dont use page.locator, instead use page.frame_locator
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link",name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text(" Happy Subscibers!")
