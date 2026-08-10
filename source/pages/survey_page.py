from playwright.sync_api import Page
from datetime import date
from source.pages.base_page import BasePage
from source.config.config_reader import cr
from source.locators.survey_locators import survey_elements



class EPC_Survey_Page:
    def __init__(self, page:Page):
        self.page = page
    
    
    def navigate_to_survey_page(self):
        self.page.locator("(//i-feather[@class='icon-people'])[1]").hover()
        self.page.locator("a").filter(has_text="Project Management ").click()
        self.page.get_by_role("link", name="Site Survey").click()
        # self.page.wait_for_url('**/survey-assignment')
        self.page.locator("//div//small[text()=' Pending Assignment ']").hover()
    
    def assign_new_survey(self, project_code):
        self.page.locator("//div//small[text()=' Pending Assignment ']").hover()
        self.page.get_by_role("textbox", name="Search").click()
        self.page.get_by_role("textbox", name="Search").fill(project_code)
        self.page.get_by_role("textbox", name="Search").press("Enter")
        self.page.wait_for_timeout(1000)
        self.page.locator("(//p-button[@icon='pi pi-ellipsis-v']//button)[1]").click()
        self.page.locator("a").filter(has_text="Assign Survey").click()
        self.page.locator("//p-datepicker[@formcontrolname='request_date']//input").click()
        today = date.today()
        formatted_date = today.strftime("%d-%m-%Y")
        self.page.locator(survey_elements.request_date).type(formatted_date)
        self.page.locator(survey_elements.request_date).press("Enter")
        self.page.get_by_role("textbox", name="Site Address ").click()
        self.page.get_by_role("textbox", name="Site Address ").fill("DEMO ADDRESS")
        self.page.get_by_role("textbox", name="GPS Coordinates (Latitude) ").click()
        self.page.get_by_role("textbox", name="GPS Coordinates (Latitude) ").fill("12.36985")
        self.page.get_by_role("textbox", name="GPS Coordinates (Longitude) ").click()
        self.page.get_by_role("textbox", name="GPS Coordinates (Longitude) ").fill("78.65294")
        self.page.get_by_role("textbox", name="Land Area (Acres) ").click()
        self.page.get_by_role("textbox", name="Land Area (Acres) ").fill("100")
        self.page.locator("//p-select[@formcontrolname='site_access']//div").click()
        self.page.get_by_text("Full", exact=True).click()
        self.page.locator("//p-select[@formcontrolname='survey_type']//div").click()
        self.page.get_by_text("Rooftop Survey").click()
        self.page.locator("//p-select[@formcontrolname='priority']//div").click()
        self.page.get_by_text("High").click()
        self.page.locator("(//button[@aria-label='Choose Date'])[2]").click()
        self.page.locator("//button[@aria-label='Next Month']").click()
        self.page.wait_for_timeout(1000)
        self.page.locator("//tbody//td//span[text()='20']").click()
        self.page.locator("#guidelines").type("DEMO SURVEY GUIDELINES")
        self.page.locator("//p-autocomplete[@formcontrolname='agency']//div//button").click()
        self.page.get_by_text("testing", exact=True).click()
        self.page.locator("//p-select[@formcontrolname='contact_person_id']//div").click()
        self.page.get_by_text("Shuja Riyaz").click()
        self.page.get_by_role("textbox", name="Contact Number ").click()
        self.page.get_by_role("textbox", name="Contact Number ").clear()
        self.page.get_by_role("textbox", name="Contact Number ").fill("985698547")
        self.page.get_by_role("textbox", name="Email Address ").click()
        self.page.get_by_role("textbox", name="Email Address ").clear()
        self.page.get_by_role("textbox", name="Email Address ").fill("TEST@gmail.com")
        self.page.get_by_role("button", name=" Upload Document").click()
        self.page.wait_for_timeout(1000)
        self.page.locator(".w-100 > .p-autocomplete > .p-ripple").click()
        self.page.get_by_role("dialog", name="Upload Document").locator("input[name=\"undefined\"]").click()
        self.page.get_by_role("dialog", name="Upload Document").locator("input[name=\"undefined\"]").fill("survey")
        self.page.get_by_text("Site Survey Report").click()
        # self.page.locator(".pi.pi-cloud-upload.upload-icon").click()
        self.page.wait_for_timeout(000)
        base_p = BasePage()
        filepath = base_p.get_file(cr.get_survey_file())
        self.page.locator("input[type=\"file\"]").set_input_files(filepath)
        self.page.get_by_role("textbox", name="Enter description").click()
        self.page.get_by_role("textbox", name="Enter description").fill("Survey description")
        self.page.get_by_role("button", name=" Upload").click()
        self.page.get_by_role("textbox", name="Remarks").click()
        self.page.get_by_role("textbox", name="Remarks").fill("Survey internal notes")
        self.page.get_by_role("button", name=" Assign & Submit").click()
    
    def submit_survey_report(self, prjct_code):
        self.page.locator("//div//small[text()=' Pending Assignment ']").hover()
        self.page.get_by_role("textbox", name="Search").click()
        self.page.get_by_role("textbox", name="Search").fill(prjct_code)
        self.page.get_by_role("textbox", name="Search").press("Enter")
        self.page.wait_for_timeout(1000)
        self.page.locator("(//p-button[@icon='pi pi-ellipsis-v']//button)[1]").click()
        self.page.locator("a").filter(has_text="Submit Report").click()
        self.page.locator("//p-datepicker[@formcontrolname='survey_completion_date']//input").click()
        today = date.today()
        formatted_date = today.strftime("%d-%m-%Y")
        self.page.locator("//p-datepicker[@formcontrolname='survey_completion_date']//input").type(formatted_date)
        self.page.locator("//p-datepicker[@formcontrolname='survey_completion_date']//input").press("Enter")
        self.page.locator("//p-select[@formcontrolname='roof_type']//div").click()
        self.page.get_by_text("Metal Sheet").click()
        self.page.get_by_role("textbox", name="Total Usable Roof Area (sq.ft").click()
        self.page.get_by_role("textbox", name="Total Usable Roof Area (sq.ft").fill("150")
        self.page.locator("//p-select[@formcontrolname='roof_orientation']//div").click()
        self.page.get_by_text("East", exact=True).click()
        self.page.locator("//p-select[@formcontrolname='shading_condition']//div").click()
        self.page.get_by_text("Partial Shading").click()
        self.page.get_by_role("textbox", name=" Recommended Capacity (kWp / MWp) ").click()
        self.page.get_by_role("textbox", name=" Recommended Capacity (kWp / MWp) ").fill("50")
        self.page.locator("//p-select[@formcontrolname='phase']//div").click()
        self.page.get_by_text("Three Phase").click()
        self.page.locator("//p-select[@formcontrolname='meter_type']//div").click()
        self.page.get_by_text("Three Phase Meter").click()
        self.page.locator("//p-select[@formcontrolname='earthing_available']//div").click()
        self.page.get_by_text("Yes").click()
        self.page.get_by_role("button", name=" Upload Document").click()
        self.page.wait_for_timeout(1000)
        self.page.locator(".w-100 > .p-autocomplete > .p-ripple").click()
        self.page.get_by_role("dialog", name="Upload Document").locator("input[name=\"undefined\"]").click()
        self.page.get_by_role("dialog", name="Upload Document").locator("input[name=\"undefined\"]").fill("survey")
        self.page.get_by_text("Site Survey Report").click()
        # self.page.locator(".pi.pi-cloud-upload.upload-icon").click()
        self.page.wait_for_timeout(000)
        base_p = BasePage()
        filepath = base_p.get_file(cr.get_survey_file())
        self.page.locator("input[type=\"file\"]").set_input_files(filepath)
        self.page.get_by_role("textbox", name="Enter description").click()
        self.page.get_by_role("textbox", name="Enter description").fill("Survey description submit step")
        self.page.locator("//button//span[text()='Upload']").click()
        self.page.get_by_role("button", name=" Submit Report").click()
        
        
        
        
        
        
        
        
        