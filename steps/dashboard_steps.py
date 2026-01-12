from behave import given, when, then

@given('Click on the PIM button on the left menu')
def steps_impl(context):
    context.dashboard_page.click_pim()

@when('Click the Add button')
def steps_impl(context):
    context.dashboard_page.click_add()

@when('Enter "{first_name_text}" in the First Name input field')
def steps_impl(context, first_name_text):
    context.dashboard_page.set_first_name(first_name_text)

@when('Enter "{last_name_text}" in the Last Name input field')
def steps_impl(context, last_name_text):
    context.dashboard_page.set_last_name(last_name_text)

@when('Click Save button')
def steps_impl(context):
    context.dashboard_page.click_save()

@then('The employee name in Personal Details page which is created is "{personal_page_name}"')
def steps_impl(context, personal_page_name):
    assert context.dashboard_page.verify_personal_page_name(personal_page_name),  f"Personal details page name error!"

#searchEmployee scenario
@when('Enter "{employee_name_text}" in the Employee Name input field')
def steps_impl(context, employee_name_text):
    context.dashboard_page.set_employee_name(employee_name_text)

@when('Click Search button')
def steps_impl(context):
    context.dashboard_page.click_search()

@then('The First (& Middle) Name in Records Found List is "{first_name_record}"')
def steps_impl(context, first_name_record):
    assert context.dashboard_page.verify_record_first_name(first_name_record),  f"First name recorded error!"

@then('The Last Name in Records Found List is "{last_name_record}"')
def steps_impl(context, last_name_record):
    assert context.dashboard_page.verify_record_last_name(last_name_record),  f"Last name recorded error!"

@when('Click Edit Profile button')
def steps_impl(context):
    context.dashboard_page.click_edit_profile()

@when('Select "{nationality}" in the Nationality select field')
def steps_impl(context, nationality):
    context.dashboard_page.select_nationality(nationality)

@when('Select "{marital_status}" in the Marital Status select field')
def steps_impl(context, marital_status):
    context.dashboard_page.select_marital_status(marital_status)

@then('The Nationality selected field is "{nationality}"')
def steps_impl(context, nationality):
    assert context.dashboard_page.verify_selected_nationality(nationality), f"Nationality selected error!"

@then('The Marital Status selected field is "{marital_status}"')
def steps_impl(context, marital_status):
    assert context.dashboard_page.verify_selected_marital_status(marital_status), f"Marital Status selected error!"

