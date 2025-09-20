import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")

def test_form(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")

    input_field = page.get_by_placeholder('What needs to be done?')
    expect(input_field).to_be_empty()

    input_field.fill("задача номер 1")
    input_field.press('Enter')
    input_field.fill("задача номер 2")
    input_field.press('Enter')
    page.pause()
    todo_item = page.get_by_test_id('todo-item')
    expect(todo_item).to_have_count(2)

    todo_item.get_by_role('checkbox').first.click()
    expect(todo_item.first).to_have_class('completed')

def test_demoqa_elements_text(page):
    page.goto("https://demoqa.com/text-box")
    # expect(page).to_have_url("https://demoqa.com/")
    # page.locator(".category-cards >> .card mt-4 top-card").first.click()

    #
    # page.locator("path").first.click()
    # page.get_by_role("listitem").filter(has_text="Text Box").click()
    # page.get_by_role("textbox", name="Full Name").click()
    # page.get_by_role("textbox", name="Full Name").fill("Andre")
    # page.get_by_role("textbox", name="Full Name").press("Tab")
    # page.get_by_role("textbox", name="name@example.com").click()
    # page.get_by_role("textbox", name="name@example.com").fill("andre@ffd.re")
    # page.get_by_role("textbox", name="Current Address").click()
    # page.get_by_role("textbox", name="Current Address").fill("MPEI")
    # page.locator("#permanentAddress").click()
    # page.locator("#permanentAddress").fill("AAM")
    # page.get_by_role("button", name="Submit").click()
    # page.get_by_text("Name:Andre").click()
    # page.get_by_text("Email:andre@ffd.re").click()
    # page.get_by_text("Current Address :MPEI").click()
    # page.get_by_text("Permananet Address :AAM").click()