from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def is_dashboard_displayed(self):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("dashboard")
        )
        return "dashboard" in self.driver.current_url.lower()
