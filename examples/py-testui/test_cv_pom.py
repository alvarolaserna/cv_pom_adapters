import pytest
from selenium.webdriver.chrome.options import Options
from testui.support.appium_driver import NewDriver, TestUIDriver
from cv_pom.frameworks import TestUICVPOMDriver
from cv_pom.cv_pom_driver import CVPOMDriver


@pytest.fixture(autouse=True)
def testui_driver():
    options = Options()
    options.add_argument("disable-user-media-security")
    options.add_argument("--force-device-scale-factor=1")
    options.add_argument("--headless")
    options.page_load_strategy = 'eager'
    driver = NewDriver().set_selenium_driver(chrome_options=options)
    driver.navigate_to("https://testdevlab.com")
    driver.get_driver().set_window_size(2000, 1440)

    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def cv_pom_driver(testui_driver):
    driver = TestUICVPOMDriver("resources/best.pt", testui_driver)
    yield driver


class TestSuite:
    def test_test_for_testdevlab(self, testui_driver: TestUIDriver, cv_pom_driver: CVPOMDriver):
        page = cv_pom_driver.get_page()
        page.element({"text": {"value": "Contact us", "case_sensitive": False}}).click()
        page.element({"text": "Accept"}).click()
        print(cv_pom_driver.get_page().elements(None))
        page = cv_pom_driver.get_page()
        page.element({"text": {"value": "Full Name", "case_sensitive": False}}).send_keys("John Doe")

        page.element({"text": {"value": "Business E-mail", "case_sensitive": False, "contains": True}}).send_keys("johndoe@example.com")
        page.element({"text": {"value": "Message", "case_sensitive": False, "contains": True}}).send_keys("This is a test message")