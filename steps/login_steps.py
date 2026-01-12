from behave import given, when, then

@given("Navigate to OrangeHRM page")
def steps_impl(context):
    context.login_page.open()

@when('Enter "{user_text}" in the username input field')
def steps_impl(context, user_text):
    context.login_page.set_username(user_text)

@when('Enter "{pass_text}" in the password input field')
def steps_impl(context, pass_text):
    context.login_page.set_password(pass_text)

@when('Click the Login button')
def steps_impl(context):
    context.login_page.click_button()

@then('The url of the new page is "{expected_url}"')
def steps_impl(context, expected_url):
    assert context.login_page.verify_new_url(expected_url),\
        f"Expected URL to be {expected_url}, but was {context.login_page.driver.current_url}"

@then('The header text of the new page is "Dashboard"')
def steps_impl(context):
    assert context.login_page.verify_header_text(), f"Header test is not Dashboard"

@then('The error text for the invalid password is "{expected_text}"')
def step_impl(context, expected_text):
    assert context.login_page.verify_login_error_message_displayed(expected_text), f"Error message was not displayed"

@then("The user remains on the Login page")
def step_impl(context):
    assert context.login_page.get_current_url() == \
           "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
