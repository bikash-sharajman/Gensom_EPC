import pytest
from source.config.config_reader import cr


@pytest.mark.testing
def test_epc_positive_flow(setup):
    setup.epc_login.login(cr.email, cr.password)
    setup.project_init.navigate_to_project_initialization()
    p_code = setup.project_init.inititate_new_project()
    print(p_code)