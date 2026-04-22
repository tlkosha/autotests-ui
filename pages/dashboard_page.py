from playwright.sync_api import Page, expect

from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

        self.students_title = page.get_by_test_id('students-widget-title-text')
        self.students_chart = page.get_by_test_id('students-bar-chart')

        self.activities_title = page.get_by_test_id('activities-widget-title-text')
        self.activities_chart = page.get_by_test_id('activities-line-chart')

        self.courses_title = page.get_by_test_id('courses-widget-title-text')
        self.courses_chart = page.get_by_test_id('courses-pie-chart')

        self.scores_title = page.get_by_test_id('scores-widget-title-text')
        self.scores_chart = page.get_by_test_id('scores-scatter-chart')


    def assert_dashboard_title(self):
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text('Dashboard')