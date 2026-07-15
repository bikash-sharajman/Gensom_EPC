import pytest

from source.browser.browser_factory import BrowserFactory

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
    
    
@pytest.fixture(scope="function")
def setup(request):
    browser_name = request.config.getoption("--browser")
    # headless_mode = bool(request.config.getoption("--headless"))
    headless_mode = (request.config.getoption("--headless").lower() == "true")
    bf = BrowserFactory()
    browser, context, page = bf.launch_browser(browser_name, headless_mode)

    yield page

    bf.close_browser(browser, context)