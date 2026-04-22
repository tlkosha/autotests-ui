from playwright.sync_api import Page

class BasePage:
    def __init__(self, page):
        self.page = page

    def visit(self, url: str): #Переход на страницу
        self.page.goto(url, wait_until="networkidle")

    def reload(self): #перезагрузка страницы
        self.page.reload(wait_until="networkidle")
