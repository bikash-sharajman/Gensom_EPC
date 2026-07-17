import pytest
from playwright.sync_api import Page
from source.browser.browser_factory import BrowserFactory
from source.pages.project_initialization_page import Project_Initialization_Page
from source.pages.login_page import EPC_Login
from source.config.config_reader import cr


class PageObjects:
    def __init__(self, page):
        self.page = page
        self.project_init = Project_Initialization_Page(page)
        self.epc_login = EPC_Login(page)
              
        
        
def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        choices=["chromium", "firefox", "webkit"],
        help="Browser name")

    parser.addoption(
        "--headless",
        action="store",
        default="false",
        choices=["true", "false"],
        help="Run browser in headless mode")
    
    
_base_url = cr.get_url()
    
@pytest.fixture(scope="function")
def setup(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = (request.config.getoption("--headless").lower() == "true")
    bf = BrowserFactory()
    browser, context, page = bf.launch_browser(browser_name, headless_mode)
    page.goto(_base_url)
    objects = PageObjects(page)

    yield objects

    bf.close_browser(browser, context)