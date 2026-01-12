from browser import Browser
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage(context.browser.driver)
    context.dashboard_page = DashboardPage(context.browser.driver)

def before_scenario(context, scenario):
    # Login automat doar pentru scenariile cu tag @dashboard
    if "dashboard" in scenario.tags:
        context.login_page.open()
        context.login_page.login("Admin", "admin123")


def after_all(context):
    context.browser.close()