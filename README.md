BDD Automation Testing Project – OrangeHRM
Overview

This repository contains a BDD (Behavior Driven Development) automated testing framework for the OrangeHRM web application, built using Python, Behave, and Selenium WebDriver.

The project demonstrates best practices in test automation, including:

BDD scenarios written in Gherkin

Page Object Model (POM) design pattern

Clear separation between features, steps, and page logic

The application under test is the official OrangeHRM demo site:
🔗 https://opensource-demo.orangehrmlive.com

Project Goals

The main objective of this project is to validate core functionalities of the OrangeHRM application, such as:

User authentication

Employee management (add, search, edit)

Dashboard functionality validation

This project is intended for learning and demonstration purposes, showcasing BDD-based automation testing skills.

 Test Coverage

✅ Automated functional tests

✅ BDD scenarios (Given / When / Then – Gherkin syntax)

❌ Negative tests (e.g. login with invalid credentials)

Technologies & Tools

Python

Behave

Selenium WebDriver

Page Object Model (POM)

Gherkin

ChromeDriver

📂 Project Structure
BDD-OrangeHRM-Project/
├── features/
│   ├── login.feature
│   ├── dashboard.feature
│
├── steps/
│   ├── login_steps.py
│   └── dashboard_steps.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
│
├── browser.py
├── environment.py
├── requirements.txt
└── README.md

How to Run the Tests

Install the required dependencies:

pip install -r requirements.txt


Run the test suite:

behave

 Author

This project was created for educational purposes, focusing on BDD automation testing and test framework design.
