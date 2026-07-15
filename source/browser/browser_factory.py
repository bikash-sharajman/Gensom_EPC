from playwright.sync_api import sync_playwright

from config.config_reader import cr


class BrowserFactory:

    def __init__(self):
        self.playwright = sync_playwright().start()

    def launch_browser(self, browser_name, headless_mode):
        # browser_name = cr.get_browser()

        browser_map = {
            "chromium": self.playwright.chromium,
            "firefox": self.playwright.firefox,
            "webkit": self.playwright.webkit
            }

        if browser_name not in browser_map:
            raise ValueError(
                f"Unsupported Browser : {browser_name}")

        browser = browser_map[browser_name].launch(
            headless=headless_mode,
            slow_mo=cr.get_slow_mo())

        context = browser.new_context()
        page = context.new_page()
        return browser, context, page

    def close_browser(self, browser, context):
        context.close()
        browser.close()
        self.playwright.stop()
        
        