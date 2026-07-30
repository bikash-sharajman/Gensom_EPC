from playwright.sync_api import Page
from datetime import date
from source.pages.base_page import BasePage
import pyautogui
from source.config.config_reader import cr
from source.locators.engineering_locators import engineering_fields



class Engineering_design_Page:
    def __init__(self, page:Page):
        self.page = page
    
    
    def navigate_to_engineering_page(self):
        self.page.wait_for_timeout(1000)
        self.page.locator("(//i-feather[@class='icon-people'])[1]").hover()
        # self.page.locator("a").filter(has_text="Project Management ").click()
        self.page.get_by_role("link", name="Engineering Design").click()
        # self.page.wait_for_url('**engineering-dash')
        self.page.locator("//div//small[text()=' Draft ']").hover()
        
    def click_on_start_design_of_project(self, project_code):
        self.page.locator("//div//small[text()=' Draft ']").hover()
        # self.page.get_by_role("textbox", name="Search").click()
        self.page.get_by_role("textbox", name="Search").fill(project_code)
        self.page.get_by_role("textbox", name="Search").press("Enter")
        self.page.locator("(//p-button[@icon='pi pi-ellipsis-v']//button)[1]").click()
        self.page.wait_for_timeout(2000)
        self.page.locator("(//p-button[@icon='pi pi-ellipsis-v']//button)[1]").click()
        self.page.locator("a").filter(has_text="Start Design").click()
        
    def click_on_submit_for_final_approval_button(self, project_code):
        # self.page.get_by_role("textbox", name="Search").click()
        self.page.get_by_role("textbox", name="Search").fill(project_code)
        self.page.get_by_role("textbox", name="Search").press("Enter")
        # self.page.wait_for_timeout(2000)
        self.page.locator("(//p-button[@icon='pi pi-ellipsis-v']//button)[1]").click()
        self.page.wait_for_timeout(2000)
        self.page.locator("(//p-button[@icon='pi pi-ellipsis-v']//button)[1]").click()
        self.page.locator("a").filter(has_text="Submit for Approval").click()       
        
    def upload_plant_layout_document(self):
        document_field = self.page.locator(engineering_fields.document_uploader)
        document_field.clear()
        document_field.type("Plant Layout")
        self.page.get_by_text("Plant Layout").click()
        # self.page.locator(".pi.pi-cloud-upload.upload-icon").click()
        # self.page.keyboard.press("Escape")
        base_p = BasePage()
        filepath = base_p.get_file(cr.get_plant_layout_file())
        self.page.locator("input[type=\"file\"]").set_input_files(filepath)
        # pyautogui.press("esc")
        self.page.get_by_role("textbox", name="Enter description").click()
        self.page.get_by_role("textbox", name="Enter description").fill("Plant layout uploaded.")
        self.page.get_by_role("button", name=" Upload").click()
        
        
    def upload_sld_document(self):
        document_field = self.page.locator(engineering_fields.document_uploader)
        document_field.clear()
        document_field.type("SLD")
        self.page.get_by_text(" Single Line Diagram (SLD) ").click()
        # self.page.locator(".pi.pi-cloud-upload.upload-icon").click()
        # self.page.keyboard.press("Escape")
        base_p = BasePage()
        filepath = base_p.get_file(cr.get_sld_file())
        self.page.locator("input[type=\"file\"]").set_input_files(filepath)
        # pyautogui.press("esc")
        self.page.get_by_role("textbox", name="Enter description").click()
        self.page.get_by_role("textbox", name="Enter description").fill("SLD file uploaded.")
        self.page.get_by_role("button", name=" Upload").click()
        
        
    def upload_structural_document(self):
        document_field = self.page.locator(engineering_fields.document_uploader)
        document_field.clear()
        document_field.type("Structural")
        self.page.get_by_text(" Structural Layout ").click()
        # self.page.locator(".pi.pi-cloud-upload.upload-icon").click()
        # self.page.keyboard.press("Escape")
        base_p = BasePage()
        filepath = base_p.get_file(cr.get_structural_file())
        self.page.locator("input[type=\"file\"]").set_input_files(filepath)
        # pyautogui.press("esc")
        self.page.get_by_role("textbox", name="Enter description").click()
        self.page.get_by_role("textbox", name="Enter description").fill("Structural file uploaded.")
        self.page.get_by_role("button", name=" Upload").click()
        
    
    def upload_foundation_document(self):
        document_field = self.page.locator(engineering_fields.document_uploader)
        document_field.clear()
        document_field.type("Foundation")
        self.page.get_by_text(" Foundation Design ").click()
        # self.page.locator(".pi.pi-cloud-upload.upload-icon").click()
        # self.page.keyboard.press("Escape")
        base_p = BasePage()
        filepath = base_p.get_file(cr.get_foundation_file())
        self.page.locator("input[type=\"file\"]").set_input_files(filepath)
        # pyautogui.press("esc")
        self.page.get_by_role("textbox", name="Enter description").click()
        self.page.get_by_role("textbox", name="Enter description").fill("Foundation file uploaded.")
        self.page.get_by_role("button", name=" Upload").click()
        
    
    def start_new_engineering_design(self):
        self.page.get_by_role("button",name="Upload Design Document").click()
        self.upload_plant_layout_document()
        self.page.get_by_role("button",name="Upload Design Document").click()
        self.upload_sld_document()
        self.page.get_by_role("button",name="Upload Design Document").click()
        self.upload_structural_document()
        self.page.get_by_role("button",name="Upload Design Document").click()
        self.upload_foundation_document()
        self.page.get_by_role("button", name=" Save For Approval").click()
        
        
        
    def submit_for_final_approval(self, p_code):
        self.page.wait_for_timeout(2000)
        self.click_on_submit_for_final_approval_button(p_code)
        self.page.locator("[id='remarks_0']").fill("done")
        self.page.locator("[id='remarks_1']").fill("done")
        self.page.locator("[id='remarks_2']").fill("done")
        self.page.locator("[id='remarks_3']").fill("done")
        self.page.get_by_role("textbox", name="Approver Comments").fill("approved")
        self.page.get_by_role("button", name="Approve").click()
        
        self.page.wait_for_timeout(50000)
        
        

        
        
        
        
    
        
        
        
        