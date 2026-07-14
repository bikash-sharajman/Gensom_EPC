import pytest

from source.browser.browser_factory import BrowserFactory


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        # choices=["chromium", "firefox", "webkit"],
        help="Browser name"
    )
    
    
@pytest.fixture(scope="function")
def setup(request):
    browser_name = request.config.getoption("--browser")
    bf = BrowserFactory()
    browser, context, page = bf.launch_browser(browser_name)

    yield page

    bf.close_browser(browser, context)