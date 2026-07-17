from playwright.sync_api import Page
from datetime import date



class Project_Initialization_Page:
    
    def __init__(self, page:Page):
        self.page = page    
    

    # def project_initialization_step(playwright: Playwright, project_code) -> None:
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context()
    #     page = context.new_page()
    #     page.goto("https://epc.demo.gensomsolar.com/login")
    #     page.get_by_role("textbox", name="Email Address Password").click()
    #     page.get_by_role("textbox", name="Email Address Password").fill("ashish.k@sharajman.com")
    #     page.get_by_role("textbox", name="Password", exact=True).click()
    #     page.get_by_role("textbox", name="Password", exact=True).fill("Gensom@1234")
    #     page.get_by_role("button", name="Login").click()
    #     page.locator("a").filter(has_text="Sales Handover").click()
    #     page.get_by_role("link", name=" Project Initialization").click()
    #     page.locator("#project_status").click()
    #     page.get_by_text("To be Initiated").click()
    #     page.get_by_role("button", name=" Apply").click()
    #     page.get_by_role("row", name="Community Center Solar").get_by_role("button").click()
    #     page.locator("a").filter(has_text="Proceed to Project").click()
    #     page.locator("#pn_id_54").get_by_role("button", name="dropdown trigger").click()
    #     page.get_by_text("Rooftop Solar").click()
    #     page.locator("#pn_id_56").get_by_role("button", name="dropdown trigger").click()
    #     page.get_by_role("option", name="Commercial").click()
    #     page.locator(".p-component.p-iconwrapper.ng-tns-c2825477640-36 > .p-icon").click()
    #     page.get_by_text("15", exact=True).click()
    #     page.get_by_role("combobox", name="Expected Completion Date").click()
    #     page.get_by_role("button", name="Next Month").click()
    #     page.get_by_text("31").nth(2).click()
    #     page.locator("#pn_id_62").get_by_role("button", name="dropdown trigger").click()
    #     page.get_by_role("option", name="Ashish Kumar").click()
    #     page.get_by_role("textbox", name="Remarks").click()
    #     page.get_by_role("textbox", name="Remarks").fill("this is automation configuration")
    #     page.get_by_role("checkbox", name="I confirm that the above").check()
    #     page.get_by_role("button", name=" Submit").click()

    #     # ---------------------
    #     context.close()
    #     browser.close()
    
    def navigate_to_project_initialization(self):
        self.page.locator("(//i-feather[@class='icon-people'])[1]").hover()
        # self.page.locator("a").filter(has_text="Sales Handover").click()
        self.page.locator("//*[@id='sidebarnav']/li[2]/a/span").click()
        
        self.page.get_by_role("link", name=" Project Initialization").click()
        self.page.wait_for_url("**/project-initialization")
        
        
        
        
    def inititate_new_project(self):
        self.page.locator("//p-select[@inputid='project_status']//div").click()
        self.page.get_by_role("option", name="To be Initiated").click()
        self.page.get_by_role("button", name=" Apply").click()
        self.page.locator("(//p-button[@icon='pi pi-ellipsis-v']//button)[1]").click()
        self.page.locator("a").filter(has_text="Proceed to Project").click()
        self.page.locator("//p-select[@formcontrolname='project_type']//div").click()
        self.page.locator("//p-selectitem//span[text()='Rooftop Solar']").click()
        self.page.locator("//p-select[@formcontrolname='project_category']//div").click()
        self.page.get_by_role("option", name="Commercial").click()
        today = date.today()
        formatted_date = today.strftime("%d-%m-%Y")
        # self.page.locator(f"//tbody//span[text() = '{day}']").click()
        self.page.locator("//input[@id='expected_start_date']").type(formatted_date)
        self.page.locator("//input[@id='expected_start_date']").press("Enter")
        self.page.locator("//*[@id='expected_completion_date']").click()
        self.page.wait_for_timeout(1000)
        self.page.locator("//button[@aria-label='Next Month']").click()
        self.page.wait_for_timeout(1000)
        self.page.locator("//tbody//td//span[text()='20']").click()
        self.page.locator("//p-select[@formcontrolname='project_head']//div").click()
        self.page.get_by_role("option", name="Ashish Kumar").click()
        self.page.get_by_role("textbox", name="Remarks").click()
        self.page.get_by_role("textbox", name="Remarks").fill("this is automation configuration")
        self.page.get_by_role("checkbox", name="I confirm that the above").check()
        self.page.get_by_role("button", name=" Submit").click()
        self.page.wait_for_timeout(1000)
        project_code = self.page.locator("(//tbody//tr/td)[1]").text_content()
        return project_code
        


