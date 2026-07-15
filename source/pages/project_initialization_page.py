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
    page.locator("a").filter(has_text="Sales Handover").click()
    page.get_by_role("link", name=" Project Initialization").click()
    page.locator("#project_status").click()
    page.get_by_text("To be Initiated").click()
    page.get_by_role("button", name=" Apply").click()
    page.get_by_role("row", name="Community Center Solar").get_by_role("button").click()
    page.locator("a").filter(has_text="Proceed to Project").click()
    page.locator("#pn_id_54").get_by_role("button", name="dropdown trigger").click()
    page.get_by_text("Rooftop Solar").click()
    page.locator("#pn_id_56").get_by_role("button", name="dropdown trigger").click()
    page.get_by_role("option", name="Commercial").click()
    page.locator(".p-component.p-iconwrapper.ng-tns-c2825477640-36 > .p-icon").click()
    page.get_by_text("15", exact=True).click()
    page.get_by_role("combobox", name="Expected Completion Date").click()
    page.get_by_role("button", name="Next Month").click()
    page.get_by_text("31").nth(2).click()
    page.locator("#pn_id_62").get_by_role("button", name="dropdown trigger").click()
    page.get_by_role("option", name="Ashish Kumar").click()
    page.get_by_role("textbox", name="Remarks").click()
    page.get_by_role("textbox", name="Remarks").fill("this is automation configuration")
    page.get_by_role("checkbox", name="I confirm that the above").check()
    page.get_by_role("button", name=" Submit").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)