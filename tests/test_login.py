from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_orangehrm_login(setup):
    login = LoginPage(setup)
    login.login("Admin", "admin123")
    print("Hello Mani")
    dashboard = DashboardPage(setup)
    assert dashboard.is_dashboard_displayed()