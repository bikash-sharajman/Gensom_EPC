import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://epc.demo.gensomsolar.com/login")
    page.get_by_role("textbox", name="Email Address Password").click()
    page.get_by_role("textbox", name="Email Address Password").fill("ashish.k@sharajman.com")
    page.get_by_role("textbox", name="Password", exact=True).click()
    page.get_by_role("textbox", name="Password", exact=True).fill("Gensom@1234")
    page.get_by_role("button", name="Login").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)