from playwright.sync_api import Page
from source.pages.base_page import base_page



class BOQ_Page:
    def __init__(self, page:Page):
        self.page = page
    
    
    def navigate_to_boq_page(self):
        self.page.wait_for_timeout(1000)
        self.page.locator("(//i-feather[@class='icon-people'])[1]").hover()
        self.page.locator("a").filter(has_text="Project Management ").click()
        self.page.get_by_role("link", name="BOQ (Material Specs)").click()
        # self.page.wait_for_url('**engineering-dash')
        self.page.locator("//div//small[text()=' Approved BOQs ']").hover()
        
    def click_on_cost_estimation_approve_button(self, project_code):
        self.page.get_by_role("textbox", name="Search").fill(project_code)
        self.page.get_by_role("textbox", name="Search").press("Enter")
        # self.page.wait_for_timeout(2000)
        self.page.locator("(//p-button[@icon='pi pi-ellipsis-v']//button)[1]").click()
        # self.page.wait_for_timeout(1000)
        self.page.locator("(//p-button[@icon='pi pi-ellipsis-v']//button)[1]").click()
        self.page.locator("a").filter(has_text="Cost Estimation & Approve").click()
        
    def select_current_date(self):
        base_page.select_current_date(self)
        
        
    def filling_BOQ_Cost_Estimation_form(self):
        self.page.locator("#boq_date").click()
        self.select_current_date()
        self.page.locator("#price_basis").fill("1000000")
        # self.page.locator("//tbody//tr[1]//td[normalize-space()='1']/following-sibling::td/input[@type='number']").fill("1000")
        self.page.locator("//tbody//tr[1]//input[@type='number']").fill("1000")
        # self.page.locator("//tbody//tr[2]//td[normalize-space()='2']/following-sibling::td/input[@type='number']").fill("2000")
        self.page.locator("//tbody//tr[2]//input[@type='number']").fill("2000")
        self.page.get_by_role("button", name="Approve").click()
        
        
        self.page.wait_for_timeout(50000)
        
        
    
        
    