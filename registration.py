from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    #Сохраняем состояние из dev-tools вкладка Application - local storage в json
    context.storage_state(path='browser-state.json')

    #Создаем новую страницу и переходим сразу на страницу авторизованного пользователя, пропустив регистрацию
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json') #Берем из файла контекст JSON
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    page.wait_for_timeout(3000)

