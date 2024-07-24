from cv_pom.frameworks import TestUICVPOMDriver
from testui.support.appium_driver import TestUIDriver


# Just for the sake of intellisense
class Context:
    driver: TestUIDriver
    cv_pom_driver: TestUICVPOMDriver
