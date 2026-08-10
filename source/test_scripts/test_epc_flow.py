import pytest
from source.config.config_reader import cr


@pytest.mark.testing
def test_epc_positive_flow(setup):
    setup.epc_login.login(cr.email, cr.password)
    # setup.project_init.navigate_to_project_initialization()
    # p_code = setup.project_init.inititate_new_project()
    p_code = "PRJ-HP-2026-0037"
    # setup.token_page.navigate_to_token_receipt_page()
    # setup.token_page.process_new_receipt(p_code)
    # setup.token_page.process_receipt_verification(p_code)
    # setup.survey.navigate_to_survey_page()
    # setup.survey.assign_new_survey(p_code)
    # setup.survey.submit_survey_report(p_code)
    # setup.engg_page.navigate_to_engineering_page()
    # setup.engg_page.click_on_start_design_of_project(p_code)
    # setup.engg_page.start_new_engineering_design()
    # setup.engg_page.submit_for_final_approval(p_code)
    # setup.engg_page.upload_drawing_item_lists(p_code)
    setup.boq_page.navigate_to_boq_page() 
    setup.boq_page.click_on_cost_estimation_approve_button(p_code)
    setup.boq_page.filling_BOQ_Cost_Estimation_form()
    
    
    
    
