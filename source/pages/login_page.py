from playwright.sync_api import Page



class EPC_Login():
    
    def __init__(self, page:Page):
        self.page = page
        
        
    def enter_email(self, email):
        self.page.get_by_role("textbox", name="Email Address Password")\
            .fill(email)
            
    def enter_password(self, password):
        self.page.get_by_role("textbox", name="Password", exact=True)\
            .type(password)
            
    def click_on_loginbutton(self):
        self.page.get_by_role("button", name="Login").click()
        self.page.wait_for_url("**/project-overview-dash")
        
        
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_on_loginbutton()
        
    