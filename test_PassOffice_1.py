import re
from playwright.sync_api import Playwright, sync_playwright, expect
from pages.login_page import LoginPage
from pages.main_page import MainPage,AccessGroupPage

def test_passoffice(page,login='admin',password='admin'):
    # создаем классы
    main_page = MainPage(page)
    login_page = LoginPage(page)
    accessgroup_page = AccessGroupPage(page)
    # логинимся и проверяем что мы попали в МОИ ЗАЯВКИ
    url = '192.168.1.143:4205'
    login = 'Playwright1'
    password = 'Playwright1'

    login_page.navigate(url)
    login_page.check_visible()
    login_page.login(login,password,url)

    # создаем ГД и проверяем, что ГД находится в поиске
    access_group_name = 'Тестовая ГД27'

    main_page.search_go('Группы доступа',url,'/reports/AccessGroup/all')
    accessgroup_page.create(access_group_name)

    # # создаем гостевую заявку на нового посетителя
    visitor_1_surname = 'Нехорошев'
    visitor_1_name = 'Алексей'
    #
    # page.get_by_role("combobox", name="Поиск").click()
    # # page.get_by_role("combobox", name="Поиск").press("ControlOrMeta+a")
    # page.get_by_role("combobox", name="Поиск").fill("мои заявки")
    # page.locator("app-table-toolbar").get_by_role("button").first.click()
    #
    # request_ID = page.get_by_role("heading", name=re.compile(r"Заявка № \d+")).text_content()
    # request_ID = re.search(r"Заявка №\s*(\d+)", request_ID).group(1)
    # print('')
    # print('ID = ',request_ID)
    #
    # page.locator("[data-test-id=\"panel-element-visitors\"]").get_by_role("button").nth(1).click()
    # # перейти data test id
    # page.get_by_role("combobox", name="Фамилия").fill(visitor_1_surname)
    # page.get_by_role("combobox", name="Имя").fill(visitor_1_name)
    # # проверить категорию
    # page.locator("[data-test-id=\"panel-save-button\"]").click()
    # page.locator("[data-test-id=\"panel-element-accessGroups\"]").get_by_role("button").click()
    # page.get_by_text(access_group_name).click()
    # page.get_by_role("button", name="В обработку").click()
    # request_PIN = page.get_by_text("Пин:").text_content()
    # request_PIN = re.search(r"Пин:\s*(\d+)", request_PIN).group(1)
    # print('PIN = ',request_PIN)
    # page.locator("[data-test-id=\"close-button\"] ").locator('input').click()
    # page.get_by_role("textbox", name="Поиск").fill(request_PIN)
    # expect(page.get_by_text(request_ID)).to_be_visible()
    #




    # выдаем пропуск по ранее созданной заявке


    # page.get_by_role("button", name="Выдать пропуск").click()
    # page.get_by_role("button", name="Согласие подписано").click()
    # page.get_by_role("textbox", name="Номер пропуска").click()
    # page.get_by_role("textbox", name="Номер пропуска").fill("5462")
    # page.get_by_role("button", name="Сохранить").click()
    # page.locator("[data-test-id=\"close-button\"]").click()
    # page.get_by_role("button", name="Clear").click()
    # page.get_by_role("combobox", name="Поиск").fill("люди")
    # page.get_by_role("link", name="Люди").click()
    # page.get_by_role("textbox", name="Поиск").click()
    # page.get_by_role("textbox", name="Поиск").fill("Нехорошев Алексей")
    # page.get_by_role("cell", name="Нехорошев А").click()
    # page.locator("lib-tree-item").filter(has_text="Отчетыkeyboard_arrow_down").locator("mat-icon").click()
    # page.locator("lib-tree-item").filter(has_text="Отчетыkeyboard_arrow_down").locator("mat-icon").click()
    # page.locator("[data-test-id=\"panel-sidebar\"] div").filter(has_text="Отчеты").nth(2).click()
    # page.locator("[data-test-id=\"panel-sidebar\"] div").filter(has_text="История пропусков").nth(2).click()
    # page.locator("app-pass-list").get_by_role("cell", name="5462").click()
    # page.locator("[data-test-id=\"close-button\"]").click()
    # page.get_by_role("button", name="Clear").click()
    # page.get_by_role("combobox", name="Поиск").fill("мои заявки")
    # page.get_by_role("cell", name="Нехорошев А").click()
    # page.get_by_role("button", name="Аннулировать").click()
    # page.get_by_role("button", name="Clear").click()
    # page.get_by_role("combobox", name="Поиск").fill("люди")
    # page.locator("div").filter(has_text=re.compile(r"^Поиск$")).nth(4).click()
    # page.get_by_role("textbox", name="Поиск").fill("Нехорошев Алексей")
    # page.get_by_role("cell", name="Нехорошев А").click()
    # page.locator("[data-test-id=\"panel-sidebar\"] div").filter(has_text="Отчеты").nth(2).click()
    # page.locator("[data-test-id=\"panel-sidebar\"] div").filter(has_text="История пропусков").nth(2).click()
    # page.locator("[data-test-id=\"close-button\"]").click()
    # page.get_by_role("button", name="Clear").click()
    # page.get_by_role("link", name="Мои заявки").click()
    # page.get_by_role("cell", name="Отмена").click()
    # page.locator("[data-test-id=\"close-button\"]").click()


def create_AccessGroup(page):
    page.goto("http://192.168.1.143:4205/auth/login")