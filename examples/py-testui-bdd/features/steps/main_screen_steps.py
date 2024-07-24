"""Module providing Step Methods for Main Screen"""
from behave import step
from testui.elements.testui_element import e
from features.steps import Context


@step("I am in landing page")
def checks_main_page(context: Context):
    page = context.cv_pom_driver.get_page()
    page.element({"text": "Contact us"}).wait_visible()
    page.element({"text": "Accept"}).wait_visible()


@step("I click on {text}")
def click_on_by_text(context: Context, text):
    context.cv_pom_driver.element({"text": {"value": text, "contains": True}}).click()


@step("I Accept Cookies")
def click_on_accept_cookies(context: Context):
    # This uses regular UI automation, instead of CV
    context.cv_pom_driver.element({"text": "Accept"}).click()


@step("I put data: {name} and {email}")
def i_write(context: Context, name, email):
    page = context.cv_pom_driver.get_page()
    page.element({"text": {"value": "Full Name", "contains": True}}).send_keys(name)
    page.element({"text": {"value": "Business E-mail", "contains": True}}).send_keys(email)


@step("I send keys to: {field} with text: {value}")
def i_write_ocr(context: Context, field, value):
    context.cv_pom_driver.element({"text": {"value": field, "contains": True}}).send_keys(value)


@step("Text {text} is visible")
def text_visible(context: Context, text):
    context.cv_pom_driver.element({"text": {"value": text, "contains": True}}).wait_visible()
