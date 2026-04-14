from asyncio import timeout

from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False) #headless=False - значит запуск браузера с интерфейсом
    page = browser.new_page() #команда для открытия новой страницы браузера

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    button_registration = page.get_by_test_id('registration-page-registration-button')
    button_registration.click()


    header_dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(header_dashboard).to_be_visible()
    expect(header_dashboard).to_have_text('Dashboard')

    page.wait_for_timeout(2000)




