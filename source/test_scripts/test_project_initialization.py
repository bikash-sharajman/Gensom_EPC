import pytest


@pytest.mark.testing
def test_initiate_project_from_lead(setup):
    setup.project_init.navigate_to_project_initialization()