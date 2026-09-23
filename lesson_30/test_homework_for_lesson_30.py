import allure

# now Allure decorator is used for test
# also all four steps are calling right here for better Allure-report traceability
@allure.feature("User Registration")
def test_user_registration(home_page, signup_modal, garage_page, user_data):
    home_page.open_signup_modal()
    signup_modal.fill_signup_form(user_data)
    signup_modal.submit_registration()
    garage_page.assert_is_open()
