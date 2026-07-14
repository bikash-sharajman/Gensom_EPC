from playwright.sync_api import expect
from source.config.config_reader import cr
import pytest


@pytest.mark.testing
def test_epc_login(setup):
    setup.goto("https://release.gensomsolar.com/login")
    expect(setup).to_have_title("Login")
    # setup.wait_for_timeout(5000)