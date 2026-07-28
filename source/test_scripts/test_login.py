from playwright.sync_api import expect
from source.config.config_reader import cr
import pytest


@pytest.mark.testing
def test_epc_login(setup):
    setup.epc_login.login(cr.get_email_id, cr.get_password)
    