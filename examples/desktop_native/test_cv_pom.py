import pytest
from cv_pom.frameworks import DesktopCVPOMDriver
from cv_pom.cv_pom_driver import CVPOMDriver
import os


@pytest.fixture(autouse=True)
def cv_pom_driver():
    os.system("open -na \"Google Chrome\" --args --incognito \"https://www.testdevlab.com\"")
    driver = DesktopCVPOMDriver("resources/best.pt", **{'ocr': {'paragraph': False, 'canvas_size': 1200}, "resize": 0.5})
    yield driver


class TestSuite:
    def test_test_for_MAC_OS(self, cv_pom_driver: CVPOMDriver):
        page = cv_pom_driver.get_page()
        page.element({"text": {"value": "Contact us", "case_sensitive": False}}).click()
        page.element({"text": "Accept"}).click()
        print(cv_pom_driver.get_page().elements(None))
        page = cv_pom_driver.get_page()
        page.element({"text": {"value": "Full Name", "case_sensitive": False}}).send_keys("John Doe")

        page.element({"text": {"value": "Business E-mail", "case_sensitive": False, "contains": True}}).send_keys("johndoe@example.com")
        page.element({"text": {"value": "Message", "case_sensitive": True, "contains": True}}).swipe_to('down').send_keys("This is a test message")