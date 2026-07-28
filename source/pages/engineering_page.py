from playwright.sync_api import Page
from datetime import date
from source.pages.base_page import BasePage
import pyautogui



class Engineering_design_Page:
    def __init__(self, page:Page):
        self.page = page
    
    
    def navigate_to_engineering_page(self):
        self.page.locator("(//i-feather[@class='icon-people'])[1]").hover()
        self.page.locator("a").filter(has_text="Project Management").click()
        self.page.get_by_role("link", name="Engineering Design").click()
        self.page.wait_for_url('**engineering-dash')
        
    def click_on_start_design_of_project(self, project_code):
        self.page.locator("//div//small[text()=' Draft ']").hover()
        self.page.get_by_role("textbox", name="Search").click()
        self.page.get_by_role("textbox", name="Search").fill(project_code)
        self.page.get_by_role("textbox", name="Search").press("Enter")
        self.page.wait_for_timeout(1500)
        self.page.locator("//p-button[@icon='pi pi-ellipsis-v']//button").click()
        self.page.locator("a").filter(has_text="Start Design").click()
        
        
    def upload_plant_layout_document(self):
        self.page.locator("//p-autocomplete[@formcontrolname='documentType']//input").type("Plant Layout")
        self.page.get_by_text("Plant Layout").click()
        # self.page.locator(".pi.pi-cloud-upload.upload-icon").click()
        # self.page.keyboard.press("Escape")
        base_p = BasePage()
        filepath = base_p.get_file("source/data_files/M06 Engineering Design & Layout V1.1.pdf")
        self.page.locator("input[type=\"file\"]").set_input_files(filepath)
        # pyautogui.press("esc")
        self.page.get_by_role("textbox", name="Enter description").click()
        self.page.get_by_role("textbox", name="Enter description").fill("Survey description submit step")
        
        
    
    def start_new_engineering_design(self):
        self.page.get_by_role("button",name="Upload Design Document").click()
        self.upload_plant_layout_document()
        
        self.page.wait_for_timeout(50000)
        
    
        
        
        
        