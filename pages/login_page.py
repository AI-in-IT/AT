from playwright.sync_api import Page,Playwright, sync_playwright, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_input = page.get_by_role("textbox", name="Логин")
        self.password_input = page.get_by_role("textbox", name="Пароль")
        self.login_button = page.get_by_role("button", name="Войти")


    def navigate(self,url):
        self.page.goto("http://" + url + "/auth/login")
        expect(self.page).to_have_url("http://" + url + "/auth/login")
    def check_visible(self):
        expect(self.login_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.login_button).to_be_visible()

    def login(self, login='admin', password='admin', url='192.168.1.143'):
        # self.navigate(url)
        self.login_input.fill(login)
        expect(self.login_input).to_have_value(login)
        self.password_input.fill(login)
        expect(self.password_input).to_have_value(password)

        self.login_button.click()
        expect(self.page).to_have_url("http://" + url + "/reports/Request/myRequestsAll")