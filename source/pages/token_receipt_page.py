from playwright.sync_api import Page
from datetime import date
from source.pages.base_page import BasePage
from source.config.config_reader import cr



class Token_Receipt_Page:
    def __init__(self, page:Page):
        self.page = page
    
    
    def navigate_to_token_receipt_page(self):
        self.page.locator("(//i-feather[@class='icon-people'])[1]").hover()
        self.page.locator("a").filter(has_text="Finance ").click()
        self.page.get_by_role("link", name="Token Money Receipt").click()
        # self.page.wait_for_url('**/survey-assignment')
        self.page.locator("//div//small[text()='Submitted Receipts']").hover()
        
    def process_new_receipt(self, project_code):
        self.page.get_by_role("textbox", name="Search").fill(project_code)
        self.page.get_by_role("textbox", name="Search").press("Enter")
        self.page.locator("(//p-button[@icon='pi pi-ellipsis-v']//button)[1]").hover()
        self.page.wait_for_timeout(1000)
        self.page.locator("(//p-button[@icon='pi pi-ellipsis-v']//button)[1]").click()
        self.page.locator("a").filter(has_text="Process Receipt").click()
        self.page.locator("//p-datepicker//input[@name='receipt_date']").click()
        receipt_date = date.today()
        previous_month = receipt_date.month - 1
        formatted_date = f"{receipt_date.year}-{previous_month}-{receipt_date.day}"
        self.page.locator(f"//tbody//span[@data-date='{formatted_date}']").click()
        self.page.get_by_role("textbox", name="Amount Received").click()
        self.page.get_by_role("textbox", name="Amount Received").type("100000")
        self.page.locator("//p-select[@formcontrolname='payment_mode']//div ").click()
        self.page.get_by_role("option", name="CASH").click()
        self.page.get_by_role("textbox", name="Transaction Reference").click()
        self.page.get_by_role("textbox", name="Transaction Reference").type("OTIUYTTHJGJHGJ")
        self.page.locator("//p-select[@formcontrolname='bank_name']//div").click()
        self.page.get_by_text("State Bank of India").click()
        self.page.get_by_role("textbox", name=" Bank Account ").click()
        self.page.get_by_role("textbox", name=" Bank Account ").type("999987461518")
        self.page.get_by_role("textbox", name=" Bank Reference / UTR ").click()
        self.page.get_by_role("textbox", name=" Bank Reference / UTR ").type("SBI98798798")
        self.page.get_by_role("textbox", name="Remarks").click()
        self.page.get_by_role("textbox", name="Remarks").type("Receipt details added")
        self.page.get_by_role("button", name="Upload Document").click()
        self.page.locator("//p-autocomplete[@formcontrolname='documentType']//input").fill("Token")
        self.page.get_by_text("Token Receipt", exact=True).click()
        base_p = BasePage()
        filepath = base_p.get_file(cr.get_token_file())
        self.page.locator("//input[@type='file']").set_input_files(filepath)
        self.page.get_by_role("textbox", name="Enter description").click()
        self.page.get_by_role("textbox", name="Enter description").fill("Receipt document uploaded.")
        self.page.locator("//p-button//span[normalize-space()='Upload']").click()
        self.page.get_by_role("button", name="Save Receipt").click()
        
    def process_receipt_verification(self, project_code):
        self.page.get_by_role("textbox", name="Search").fill(project_code)
        self.page.get_by_role("textbox", name="Search").press("Enter")
        self.page.locator("(//p-button[@icon='pi pi-ellipsis-v']//button)[1]").hover()
        self.page.wait_for_timeout(1000)
        self.page.locator("(//p-button[@icon='pi pi-ellipsis-v']//button)[1]").click()
        self.page.locator("a").filter(has_text="Verification").click()
        self.page.locator("#verification-1").check()
        self.page.get_by_role("textbox", name="Remarks for Amount matches").click()
        self.page.get_by_role("textbox", name="Remarks for Amount matches").type("verified")
        self.page.locator("#verification-2").check()
        self.page.get_by_role("textbox", name="Remarks for UTR / Transaction").click()
        self.page.get_by_role("textbox", name="Remarks for UTR / Transaction").type("verified")
        self.page.locator("#verification-3").check()
        self.page.get_by_role("textbox", name="Remarks for Bank credit").click()
        self.page.get_by_role("textbox", name="Remarks for Bank credit").type("verified")
        self.page.locator("#verification-4").check()
        self.page.get_by_role("textbox", name="Remarks for Documents").click()
        self.page.get_by_role("textbox", name="Remarks for Documents").type("verified")
        self.page.locator("#verification-5").check()
        self.page.get_by_role("textbox", name="Remarks for No duplicate").click()
        self.page.get_by_role("textbox", name="Remarks for No duplicate").type("verified")
        self.page.get_by_role("textbox", name="Finance Remarks").click()
        self.page.get_by_role("textbox", name="Finance Remarks").type("Verified by finance team")
        self.page.get_by_role("button", name="Verify Receipt").click()
        