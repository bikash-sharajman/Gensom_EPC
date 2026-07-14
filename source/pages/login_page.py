from playwright.sync_api import sync_playwright

from source.locators.login import email_field

class Login_Page:
    
    
    def test_login_epc(page):
        page.locator(email_field).type("bikashsahoo")





