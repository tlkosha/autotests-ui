#Ввод текста с клавиатуры в поле
from xml.sax import parse

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus() 

    for char in 'user@gmail.com':  #вводим по одному символу из строки в поле с задержкой 200мс
        page.keyboard.type(char, delay=200)


    page.keyboard.press("ControlOrMeta+A") #нажимаем Ctrl+А - выделяем весь текст в поле

    page.wait_for_timeout(2000)
