from playwright.sync_api import Page
from datetime import date
from source.pages.base_page import BasePage
from source.config.config_reader import cr


class Vendor_Management:
    def __init__(self, page:Page):
        self.page = page
    
    def navigate_to_vendor_management(self):
        self.page.locator("(//i-feather[@class='icon-people'])[1]").hover()
        self.page.locator("a").filter(has_text="Management").nth(1).click()
        self.page.get_by_role("link", name="Vendor Management").click()
        self.page.locator("//div//small[text()=' Active Vendors ']").hover()
        
    def add_new_vendor(self):
        
        
        
        
        
        pass