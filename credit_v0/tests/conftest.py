import os
from datetime import datetime

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Page

load_dotenv()
DOMAIN = os.getenv("DOMAIN")
PROTOCOL = os.getenv("PROTOCOL")
BASE_URL = f'{PROTOCOL}://{DOMAIN}'
PASS_ALL_ACC = os.getenv("PASS_ALL_ACC")
HEADLESS = False


def pytest_configure(config):
    if config.getoption("--html"):
        report_file = f"report/playwright/report-{datetime.now().strftime('%Y%m%d%H%M%S')}.html"
        config.option.htmlpath = report_file


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()


@pytest.fixture(scope='function', autouse=True)
def initial_action(request, page: Page):
    params = request.param if hasattr(request, 'param') else {}
    username = params.get('username', ' test_user')
    password = params.get('password', f'{PASS_ALL_ACC}')

    page.goto(f'{BASE_URL}/credit/login/')
    assert page.url == f'{BASE_URL}/credit/login/', f"Failed to log in, current URL: {page.url}"
    page.fill('[name="username"]', username)
    page.fill('[name="password"]', password)
    page.click('.login-button')
    yield
