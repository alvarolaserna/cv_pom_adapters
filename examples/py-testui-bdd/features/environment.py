"""Module providing Environment Setup/TearDown"""
from datetime import datetime
import glob
import os
import allure

from cv_pom.frameworks import TestUICVPOMDriver
from testui.support.appium_driver import NewDriver
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options
from allure_behave.hooks import allure_report
from features.steps import Context


def before_all(context: Context):
    """Before all - Cleaning artifacts folder"""
    reports = glob.glob("features/artifacts/reports/*")
    screenshots = glob.glob("features/artifacts/screenshots/*")
    folders = [reports, screenshots]

    try:
        for folder in folders:
            for file in folder:
                os.remove(file)
    except OSError:
        print("-- Reports folder empty --")

    # Creating folder for screenshots
    try:
        os.mkdir("features/artifacts/screenshots")
    except OSError as _error:
        pass


def before_scenario(context: Context, scenario):
    """SetUP Drivers and CV_POM for Test Scenarios Execution"""
    print(f"-- Start Scenario: {scenario} --")

    # This are capabilities for Chrome browser testing
    options = Options()
    options.add_argument("disable-user-media-security")
    options.add_argument("--force-device-scale-factor=1")
    options.page_load_strategy = 'eager'
    context.driver = NewDriver().set_logger().set_selenium_driver(chrome_options=options)
    context.driver.navigate_to("https://testdevlab.com")
    # context.driver.get_driver.maximize_window() # Not sure why, but user input is not found in full screen for me
    context.cv_pom_driver = TestUICVPOMDriver("../../resources/best.pt", context.driver)
    # Finish chrome config


def after_scenario(context: Context, scenario):
    """TearDown Drivers for Test Execution"""
    print(f"-- End Scenario: {scenario} --")
    test_datetime = datetime.now().strftime("%d%m%Y%H%M%S")
    screenshot_name = f"{scenario.name}_{scenario.status}_{test_datetime}.png"

    context.driver.save_screenshot(f"features/artifacts/screenshots/{screenshot_name}")
    if scenario.status == "failed":
        allure.attach(
            context.driver.get_driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG
        )
    context.driver.quit()


def after_feature(_context, _feature):
    """TearDown Fixtures for Test Execution Feature"""
    allure_report("features/artifacts/reports")
