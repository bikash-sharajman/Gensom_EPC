import pytest
from source.config.config_reader import cr


@pytest.mark.testing
def test_epc_positive_flow(setup):
    setup.epc_login.login(cr.email, cr.password)
    setup.project_init.navigate_to_project_initialization()
    p_code = setup.project_init.inititate_new_project()
    # p_code = "PRJ-TN-2026-0019"
    setup.survey.navigate_to_survey_page()
    setup.survey.assign_new_survey(p_code)
    setup.survey.submit_survey_report(p_code)
    setup.engg_page.navigate_to_engineering_page()
    setup.engg_page.click_on_start_design_of_project(p_code)
    setup.engg_page.start_new_engineering_design()
    setup.engg_page.submit_for_final_approval(p_code)
    
    
    
    
