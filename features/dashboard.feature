Feature: Verify the functionality of the dashboard page

  Background: Open EmployeeList page
     Given Click on the PIM button on the left menu

  @dashboard
  @addEmployee
  Scenario: Add a new employee with valid data
    When Click the Add button
    And Enter "Ion" in the First Name input field
    And Enter "Popescu" in the Last Name input field
    And Click Save button
    Then The employee name in Personal Details page which is created is "Ion Popescu"


  @dashboard
  @searchEmployee
  Scenario: Search for an employee in records list
    When Enter "Ion Popescu" in the Employee Name input field
    And Click Search button
    Then The First (& Middle) Name in Records Found List is "Ion"
    And The Last Name in Records Found List is "Popescu"


  @dashboard
  @editEmployeeProfile
  Scenario: Edit and update employee profile
    When Enter "Ion Popescu" in the Employee Name input field
    And Click Search button
    And Click Edit Profile button
    And Select "Romanian" in the Nationality select field
    And Select "Married" in the Marital Status select field
    And Click Save button
    Then The Nationality selected field is "Romanian"
    And The Marital Status selected field is "Married"



