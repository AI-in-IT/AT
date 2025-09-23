from playwright.sync_api import Page,Playwright, sync_playwright, expect
import re

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_toggle = page.locator("app-toggle-menu").get_by_role("button")
        self.search_input = page.get_by_role("combobox", name="Поиск")

    def search(self, text):
        expect(self.menu_toggle).to_be_visible()
        if not self.search_input.is_visible():
            self.menu_toggle.click()
            expect(self.search_input).to_be_visible()
        self.search_input.fill(text)
        expect(self.search_input).to_have_value(text)

    def search_click(self, text,url=None,url_end=None):
        expect(self.page.get_by_role("link", name=text)).to_be_visible()
        self.page.get_by_role("link", name=text).click()
        if url!=None and url_end!=None:
            expect(self.page).to_have_url("http://" + url + url_end)


    def search_go(self,text,url=None,url_end=None):
        self.search(text)
        self.search_click(text,url=None,url_end=None)

class AccessGroupPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_button = page.locator("app-table-toolbar").get_by_role("button").first
        self.name_input = page.locator("[data-test-id='panel-element-name'] input")
        self.save_button = page.locator("[data-test-id='panel-save-button']")
        self.active_checkbox = page.locator("[data-test-id='panel-element-active'] input")
        self.search_input = page.get_by_role("textbox", name="Поиск")

    def create(self, name):
        expect(self.add_button).to_be_visible()
        self.add_button.click()
        expect(self.name_input).to_be_visible()
        expect(self.save_button).to_be_visible()
        expect(self.active_checkbox).to_be_visible()
        self.name_input.fill(name)
        expect(self.name_input).to_have_value(name)
        expect(self.active_checkbox).to_be_checked()
        self.save_button.click()
        expect(self.name_input).to_be_hidden()
        expect(self.save_button).to_be_hidden()
        expect(self.active_checkbox).to_be_hidden()
        self.check(name)
    def check(self,name):
        expect(self.search_input).to_be_visible()
        self.search_input.fill(name)
        expect(self.search_input).to_have_value(name)
        expect(self.page.get_by_text(name)).to_have_count(1)
        expect(self.page.get_by_text(name)).to_be_visible()

class RequestPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_button = page.locator("app-table-toolbar").get_by_role("button").first
        self.name_input = page.locator("[data-test-id='panel-element-name'] input")
        self.save_button = page.locator("[data-test-id='panel-save-button']")
        self.active_checkbox = page.locator("[data-test-id='panel-element-active'] input")
        self.search_input = page.get_by_role("textbox", name="Поиск")



    def get_ID(self):
        request_ID = self.page.get_by_role("heading", name=re.compile(r"Заявка № \d+")).text_content()
        request_ID = re.search(r"Заявка №\s*(\d+)", request_ID).group(1)
        return request_ID