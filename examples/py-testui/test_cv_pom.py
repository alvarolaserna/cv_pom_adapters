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
    # options.add_argument("--headless")
    driver = NewDriver().set_selenium_driver(chrome_options=options)
    driver.navigate_to("https://testdevlab.com")

    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def cv_pom_driver(testui_driver):
    driver = TestUICVPOMDriver("resources/best.pt", testui_driver)
    yield driver


class TestSuite:
    def test_test_for_testdevlab(self, testui_driver: TestUIDriver, cv_pom_driver: CVPOMDriver):
        # Prompt: click in contact us
        cv_pom_driver.element({"text": "Contact us"}).click()
        # Prompt: click on Accept
        cv_pom_driver.element({"text": "Accept"}).click()
        # Prompt: enter random credentials in Full name, Business E-mail and Message
        # Enter random credentials in Full Name
        cv_pom_driver.element({"text": "Full Name"}).send_keys("John Doe")

        # Enter random credentials in Business E-mail
        cv_pom_driver.element({"text": "Business E-mail"}).send_keys("johndoe@example.com")

        # Enter random credentials in Message
        cv_pom_driver.element({"text": "Message"}).send_keys("This is a test message")