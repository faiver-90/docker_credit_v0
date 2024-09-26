import re

import pytest
from dotenv import load_dotenv
from playwright.sync_api import expect, Page

from apps.questionnaire.tests.conftest import PASS_ALL_ACC, BASE_URL

load_dotenv()


# pytest -s apps.questionnaire/tests/playwright/test_pw.py::TestUsers::test_create_delete_user

class TestFastTest:
    def test_consumer_kafca_while_cicle(self, page: Page):
        pass


class TestCommonButton:
    HOME_ICON = '[data-testid="home_icon"]'
    HOME_BUTTON_URL = f'{BASE_URL}/credit/'

    def test_home_button(self, page: Page):
        page.click(self.HOME_ICON)
        expect(page).to_have_url(self.HOME_BUTTON_URL)


class TestUsers:
    USER_NAME_TEST = 'test_user'
    EMAIL = f'{USER_NAME_TEST}@gmail.com'

    DC_VALUE = '2'
    USER_NAME = 'user_name'
    USER_LASTNAME = 'user_lastname'
    USER_MIDDLENAME = 'user_middlename'
    DATE_OF_BIRTH = '2024-07-30'
    PHONE_NUMBER = '1234567890'
    PASSPORT_SERIES_MANAGER = '4010'
    PASSPORT_NUMBER_MANAGER = '123456'
    DIVISION_CODE_MANAGER = '123-456'
    ISSUED_BY_MANAGER = 'TP-17'
    ISSUE_DATE_MANAGER = '2024-07-30'
    CHECK_DATE = 'July 30, 2024'
    CHECK_PHONE = '+7 (123) 456-78-90'
    EXPECTED_DEALERSHIP = 'дц 2 1'

    # Locators
    DEALERSHIP_CENTER_TABLE_LOCATOR = '[data-label="dealership"]'
    STATUS_TABLE_LOCATOR = '[data-label="status"]'
    ISSUE_DATE_TABLE_LOCATOR = '[data-label="date_of_birth"]'
    ICON_CREATE_USER = 'icon_create_user'
    CREATE_USER_BUTTON = 'create_user'
    ICON_USERS = 'icon_users'
    USERS_BUTTON = 'users'
    DELETE_USER_BUTTON = '#delete-user'
    CONFIRM_DELETE_BUTTON = '#confirmDeleteDocumentButton'
    ROLE_FIELD = '[name="role_manager"]'
    ORGANIZATION_FIELD = '[name="organization_manager"]'
    EMAIL_FIELD = '[name="email"]'
    PASSPORT_SERIES_FIELD = '[name="passport_series_manager"]'
    PASSPORT_NUMBER_FIELD = '[name="passport_number_manager"]'
    DIVISION_CODE_FIELD = '[name="division_code_manager"]'
    ISSUED_BY_FIELD = '[name="issued_by_manager"]'
    ISSUE_DATE_FIELD = '[name="issue_date_manager"]'
    FIRST_NAME_FIELD = '[name="first_name_manager"]'
    LAST_NAME_FIELD = '[name="last_name_manager"]'
    MIDDLE_NAME_FIELD = '[name="middle_name_manager"]'
    DATE_OF_BIRTH_FIELD = '[name="date_of_birth_manager"]'
    PHONE_NUMBER_FIELD = '[name="phone_number_manager"]'
    DEALERSHIP_FIELD = '[name="dealership_manager"]'
    STATUS_FIELD = '[name="status_manager"]'
    MY_PROFILE_BUTTON = '[data-testid="my_profile"]'
    SAVE_CHANGES_BUTTON = '#submit-edit-user'

    @staticmethod
    def find_click_user_in_table(username, page):
        user_found = False
        while not user_found:
            rows = page.query_selector_all('table.table-striped.table-hover tbody tr')
            for row in rows:
                username_cell = row.query_selector('td[data-label="username"]').inner_text()
                if username_cell == username:
                    row.click()
                    return True
            next_button = page.get_by_role('link', name='Next')
            if next_button.is_visible() and next_button.is_enabled():
                next_button.click()
            else:
                break
        return False

    def go_to_users_list_click_user(self, page, username):
        page.hover(f'[data-testid="{self.ICON_USERS}"]')
        page.get_by_test_id(self.USERS_BUTTON).click()
        user_found = self.find_click_user_in_table(username, page)
        assert user_found, f"User {username} was not found in the table"

    @pytest.mark.parametrize('initial_action', [{'username': 'owner_1', 'password': f'{PASS_ALL_ACC}'}], indirect=True)
    def test_create_delete_user(self, page: Page):

        def register_user(user_name):
            page.hover(f'[data-testid="{self.ICON_CREATE_USER}"]')
            page.get_by_test_id(self.CREATE_USER_BUTTON).click()

            page.fill('[name="username"]', user_name)
            page.fill(self.EMAIL_FIELD, self.EMAIL)
            page.fill('[name="password1"]', PASS_ALL_ACC)
            page.fill('[name="password2"]', PASS_ALL_ACC)

            page.get_by_role('button', name='Зарегистрировать').click()

        register_user(self.USER_NAME_TEST)

        if page.get_by_text('A user with that username already exists.').is_visible():
            counter = 1
            while page.get_by_text('A user with that username already exists.').is_visible():
                counter += 1
                user_name_with_suffix = f"{self.USER_NAME_TEST}{counter}"
                register_user(user_name_with_suffix)
                user_name = user_name_with_suffix

        expect(page).to_have_url(f'{BASE_URL}/credit/users/')
        user_found = self.find_click_user_in_table(user_name, page)
        assert user_found, f"User {user_name} was not found in the table"

        page.on("dialog", lambda dialog: dialog.accept())

        with page.expect_navigation():
            page.click(self.DELETE_USER_BUTTON)

        user_still_exists = self.find_click_user_in_table(user_name, page)
        assert not user_still_exists, f"User {user_name} was not deleted from the table"

    @pytest.mark.parametrize('initial_action', [{'username': 'owner_1', 'password': f'{PASS_ALL_ACC}'}], indirect=True)
    def test_change_values_test_user(self, page: Page):
        self.go_to_users_list_click_user(page, self.USER_NAME_TEST)

        user_row_locator = page.locator(f'tr[data-username="{self.USER_NAME_TEST}"]')
        dealership_center_locator = user_row_locator.locator(self.DEALERSHIP_CENTER_TABLE_LOCATOR)
        status_table_locator = user_row_locator.locator(self.STATUS_TABLE_LOCATOR)
        issue_date_locator = user_row_locator.locator(self.ISSUE_DATE_TABLE_LOCATOR)

        page.fill(self.EMAIL_FIELD, '')
        page.fill(self.FIRST_NAME_FIELD, '')
        page.fill(self.LAST_NAME_FIELD, '')
        page.fill(self.MIDDLE_NAME_FIELD, '')
        page.fill(self.DATE_OF_BIRTH_FIELD, '')
        page.fill(self.PHONE_NUMBER_FIELD, '')
        page.fill(self.PASSPORT_SERIES_FIELD, '')
        page.fill(self.PASSPORT_NUMBER_FIELD, ' ')
        page.fill(self.DIVISION_CODE_FIELD, '')
        page.fill(self.ISSUED_BY_FIELD, '')
        page.fill(self.ISSUE_DATE_FIELD, '')
        page.locator(self.DEALERSHIP_FIELD).select_option([])
        if page.is_checked(self.STATUS_FIELD):
            page.click(self.STATUS_FIELD)
        page.wait_for_timeout(1000)
        page.click(self.SAVE_CHANGES_BUTTON)
        expect(status_table_locator).to_have_text('Отключен')

        self.find_click_user_in_table(self.USER_NAME_TEST, page)
        page.fill(self.EMAIL_FIELD, self.EMAIL)
        page.fill(self.FIRST_NAME_FIELD, self.USER_NAME)
        page.fill(self.LAST_NAME_FIELD, self.USER_LASTNAME)
        page.fill(self.MIDDLE_NAME_FIELD, self.USER_MIDDLENAME)
        page.fill(self.DATE_OF_BIRTH_FIELD, self.DATE_OF_BIRTH)
        page.type(self.PHONE_NUMBER_FIELD, self.PHONE_NUMBER)
        page.locator(self.DEALERSHIP_FIELD).select_option(value='2')
        page.click(self.STATUS_FIELD)
        page.fill(self.PASSPORT_SERIES_FIELD, self.PASSPORT_SERIES_MANAGER)
        page.type(self.PASSPORT_NUMBER_FIELD, self.PASSPORT_NUMBER_MANAGER)
        page.type(self.DIVISION_CODE_FIELD, self.DIVISION_CODE_MANAGER)
        page.fill(self.ISSUED_BY_FIELD, self.ISSUED_BY_MANAGER)
        page.fill(self.ISSUE_DATE_FIELD, self.ISSUE_DATE_MANAGER)
        page.click(self.SAVE_CHANGES_BUTTON)

        expect(user_row_locator.locator(f'text="{self.USER_NAME}"')).to_be_visible()
        expect(user_row_locator.locator(f'text="{self.USER_LASTNAME}"')).to_be_visible()
        expect(user_row_locator.locator(f'text="{self.USER_MIDDLENAME}"')).to_be_visible()
        expect(user_row_locator.locator(f'text="{self.EMAIL}"')).to_be_visible()
        expect(issue_date_locator).to_have_text(self.CHECK_DATE)
        expect(dealership_center_locator).to_have_text(self.EXPECTED_DEALERSHIP)
        expect(status_table_locator).to_have_text('Активен')

        self.find_click_user_in_table(self.USER_NAME_TEST, page)
        expect(page.locator(self.PASSPORT_SERIES_FIELD)).to_have_value(self.PASSPORT_SERIES_MANAGER)
        expect(page.locator(self.PASSPORT_NUMBER_FIELD)).to_have_value(self.PASSPORT_NUMBER_MANAGER)
        expect(page.locator(self.DIVISION_CODE_FIELD)).to_have_value(self.DIVISION_CODE_MANAGER)
        expect(page.locator(self.ISSUED_BY_FIELD)).to_have_value(self.ISSUED_BY_MANAGER)
        expect(page.locator(self.ISSUE_DATE_FIELD)).to_have_value(self.ISSUE_DATE_MANAGER)
        expect(page.locator(self.DATE_OF_BIRTH_FIELD)).to_have_value(self.DATE_OF_BIRTH)
        expect(page.locator(self.PHONE_NUMBER_FIELD)).to_have_value(self.CHECK_PHONE)

    @pytest.mark.parametrize('initial_action', [{'username': 'owner_1', 'password': f'{PASS_ALL_ACC}'}], indirect=True)
    def test_change_role_organisation_owner(self, page: Page):
        self.go_to_users_list_click_user(page, self.USER_NAME_TEST)
        expect(page.locator(self.ROLE_FIELD)).not_to_be_visible()
        expect(page.locator(self.ORGANIZATION_FIELD)).not_to_be_visible()
        expected_url_pattern = re.compile(rf'{BASE_URL}/credit/users/edit/\d+')
        expect(page).to_have_url(expected_url_pattern)

    def test_change_role_organisation_user(self, page: Page):
        page.click(self.MY_PROFILE_BUTTON)
        expect(page.locator(self.ROLE_FIELD)).not_to_be_visible()
        expect(page.locator(self.ORGANIZATION_FIELD)).not_to_be_visible()
        expected_url_pattern = re.compile(rf'{BASE_URL}/credit/users/edit/\d+')
        expect(page).to_have_url(expected_url_pattern)

    @pytest.mark.parametrize('initial_action', [{'username': 'owner_1', 'password': f'{PASS_ALL_ACC}'}], indirect=True)
    def test_change_dc(self, page: Page):
        self.go_to_users_list_click_user(page, self.USER_NAME_TEST)
        page.select_option(self.DEALERSHIP_FIELD, self.DC_VALUE)
        page.wait_for_timeout(1000)
        page.click(self.SAVE_CHANGES_BUTTON)
        user_row_locator = page.locator(f'tr[data-username="{self.USER_NAME_TEST}"]')
        dealership_center_locator = user_row_locator.locator(self.DEALERSHIP_CENTER_TABLE_LOCATOR)
        expect(dealership_center_locator).to_have_text(self.EXPECTED_DEALERSHIP)


class TestQuestionnaireAndUploadClientFiles:
    ID_OFFER = 8

    # Общие контейнеры и элементы страницы
    OFFERS_CONTAINER_SELECTOR = '#offers-container'
    CARD_LIST_CONTAINER = '#offers_card_list'

    # Элементы внутри карточек предложений
    CHOICE_ID_BUTTON = f'#offers-container [data-offer-id="{ID_OFFER}"]'
    CHECKBOX_IN_CARD_OFFER = f'#offers_card_list input[data-offer-id="{ID_OFFER}"]'
    DELETE_OFFER_CARD_BUTTON = f'#offers_card_list button[data-offer-id="{ID_OFFER}"]'

    # Элементы для загрузки и удаления документов
    FILE_INPUT = 'input[name="document_files"]'
    UPLOAD_DOCS_BUTTON = 'upload_docs'
    DELETE_DOC_BUTTON = 'button[data-testid="delete_docs"]'
    DELETE_CONFIRM_BUTTON = 'button#confirmDeleteDocumentButton'
    DELETE_MODAL_LABEL = '#deleteDocumentModalLabel'

    # Элементы для управления отображением документов и модальных окон
    NEW_QUESTIONNAIRE_ICON = '[data-testid="icon_new_questionnaire"]'
    NEW_QUESTIONNAIRE_BUTTON = 'new_questionnaire'
    DOCUMENT_TYPE_SELECT = 'select[name="document_type"]'
    COLLAPSE_DOCUMENTS_BUTTON = 'button[data-bs-target="#collapseDocuments"]'
    COLLAPSE_FIRST_OFFERS_BUTTON = '[id="heading-0"]'
    COLLAPSE_EXTRA_BUTTON = '#headingExtraServices'
    COLLAPSE_PRE_COUNT_BUTTON = '#accordionCard'
    ALERT_MODAL = '#alertModal'
    ALERT_MODAL_CLOSE_BUTTON = '#alertModal .btn-secondary'
    UPLOAD_FILE_CLIENT_ANCHOR = '#upload_file_client a'
    UPLOAD_FILE_CLIENT = '#upload_file_client'
    ACCORDION_UPLOADED_DOCUMENTS = '#accordionUploadedDocuments'

    # Поля для ввода данных о цене и платежах
    CAR_PRICE = '[name="car_price_car_info"]'
    DEALER_EQUIPMENT_PRICE = '[name="dealer_equipment_price_car_info"]'
    INITIAL_PAYMENT = '[name="initial_payment"]'
    KASKO_AMOUNT = '[name="kasko_amount"]'
    GAP_AMOUNT = '[name="gap_amount"]'
    SZH_AMOUNT = '[name="szh_amount"]'
    SZH_TERM = '[name="szh_term"]'
    FINANCIAL_PRODUCTS_AMOUNT = '[name="financial_products_amount"]'
    KASKO_AMOUNT_INCLUDE = '[name="kasko_amount_include"]'
    GAP_AMOUNT_INCLUDE = '[name="gap_amount_include"]'
    SZH_TERM_INCLUDE = '[name="szh_term_include"]'
    FINANCIAL_PRODUCTS_AMOUNT_INCLUDE = '[name="financial_products_amount_include"]'
    TOTAL_LOAN_AMOUNT = '#total_loan_amount'

    # Поля для ввода информации о дополнительных услугах
    INSTALLMENT_COMMISSION_INCLUDE = '[name="installment_commission_include"]'
    SMS_NOTIFICATION_INCLUDE = '[name="sms_notification_include"]'
    SMS_NOTIFICATION_DISPLAY = '#sms_notification_display'
    INSTALLMENT_COMMISSION_DISPLAY = '#installment_commission_display'

    # Элементы для выбора условий финансирования
    FINANCING_TERM_SELECTOR = '[name="financing_term"]'
    SHOW_PARTNER_OFFERS_BUTTON = '#show-partner-offers'

    PATH_TO_FIRST_OK_FILE = 'apps/questionnaire/tests/test_files/ok_size_1.jpg'
    PATH_TO_SECOND_OK_FILE = 'apps/questionnaire/tests/test_files/ok_size_2.jpg'
    PATH_TO_OVERSIZE_FILE = 'apps/questionnaire/tests/test_files/over_size_2.jpg'
    PATH_TO_NOT_CORRECT_FORMAT_FILE = 'apps/questionnaire/tests/test_files/test_file.txt'
    DOCUMENT_TYPE = 'Водительское удостоверение'
    CHECK_INCORRECT_FORMAT_FILE_TEXT = 'Не правильный формат файла'
    CHECK_OVERSIZE_FILE = 'Файл слишком большой'
    EXPECTED_TOTAL_LOAN_AMOUNT = '38000.00'
    EXPECTED_INSTALLMENT_COMMISSION_TEXT = '✔️'
    FINANCING_TERM = '12'

    VALUES = {
        CAR_PRICE: '10000',
        DEALER_EQUIPMENT_PRICE: '20000',
        INITIAL_PAYMENT: '5000',
        KASKO_AMOUNT: '1000',
        GAP_AMOUNT: '1000',
        SZH_AMOUNT: '10000',
        SZH_TERM: '12',
        FINANCIAL_PRODUCTS_AMOUNT: '1000'
    }

    def test_card_offer(self, page: Page):
        self.navigate_to_new_questionnaire(page)
        self.show_partner_offers(page, self.FINANCING_TERM)
        page.click(self.COLLAPSE_FIRST_OFFERS_BUTTON)
        page.click(self.CHOICE_ID_BUTTON)
        page.click(self.COLLAPSE_PRE_COUNT_BUTTON)
        expect(page.locator(self.CHECKBOX_IN_CARD_OFFER)).to_be_visible()
        page.reload()
        page.click(self.COLLAPSE_PRE_COUNT_BUTTON)
        expect(page.locator(self.CHECKBOX_IN_CARD_OFFER)).to_be_visible()
        page.click(self.DELETE_OFFER_CARD_BUTTON)
        expect(page.locator(self.CARD_LIST_CONTAINER)).to_be_empty()

    def test_show_new_offers_view(self, page: Page):
        self.navigate_to_new_questionnaire(page)
        self.show_partner_offers(page, self.FINANCING_TERM)

    def test_create_new_questionnaire(self, page: Page):
        self.navigate_to_new_questionnaire(page)

    def test_calculate_total(self, page: Page):
        self.navigate_to_new_questionnaire(page)
        if not page.is_visible(self.KASKO_AMOUNT_INCLUDE):
            page.wait_for_timeout(500)
            page.click(self.COLLAPSE_EXTRA_BUTTON)

        for locator, value in self.VALUES.items():
            page.fill(locator, value)

        page.click(self.KASKO_AMOUNT_INCLUDE)
        page.click(self.GAP_AMOUNT_INCLUDE)
        page.click(self.SZH_TERM_INCLUDE)
        page.click(self.FINANCIAL_PRODUCTS_AMOUNT_INCLUDE)

        page.wait_for_function("document.querySelector('#total_loan_amount').innerText == '38000.00'")

        for locator, value in self.VALUES.items():
            expect(page.locator(locator)).to_have_value(value)
        expect(page.locator(self.TOTAL_LOAN_AMOUNT)).to_have_text(self.EXPECTED_TOTAL_LOAN_AMOUNT)

    def test_show_sms_downcoast(self, page: Page):
        self.navigate_to_new_questionnaire(page)
        if not page.is_visible(self.KASKO_AMOUNT_INCLUDE):
            page.wait_for_timeout(500)
            page.click(self.COLLAPSE_EXTRA_BUTTON)
        page.click(self.INSTALLMENT_COMMISSION_INCLUDE)
        page.click(self.SMS_NOTIFICATION_INCLUDE)
        expect(page.locator(self.SMS_NOTIFICATION_DISPLAY)).to_have_text(self.EXPECTED_INSTALLMENT_COMMISSION_TEXT)
        expect(page.locator(self.INSTALLMENT_COMMISSION_DISPLAY)).to_have_text(
            self.EXPECTED_INSTALLMENT_COMMISSION_TEXT)

    def test_one_upload_delete_client_file(self, page: Page):
        self.navigate_to_new_questionnaire(page)
        self.upload_document(page, self.DOCUMENT_TYPE, self.PATH_TO_FIRST_OK_FILE)
        expect(page.locator(self.UPLOAD_FILE_CLIENT_ANCHOR)).to_have_text(self.DOCUMENT_TYPE)

        self.delete_doc(page)

    def test_two_upload_delete_client_file(self, page: Page):
        self.navigate_to_new_questionnaire(page)
        self.upload_document(page, self.DOCUMENT_TYPE,
                             [self.PATH_TO_FIRST_OK_FILE, self.PATH_TO_SECOND_OK_FILE])
        expect(page.locator(self.UPLOAD_FILE_CLIENT_ANCHOR)).to_have_text(self.DOCUMENT_TYPE)
        self.delete_doc(page)

    def test_negative_upload_file(self, page: Page):
        self.navigate_to_new_questionnaire(page)
        self.upload_document(page, self.DOCUMENT_TYPE,
                             [self.PATH_TO_NOT_CORRECT_FORMAT_FILE])
        modal_locator = page.locator(self.ALERT_MODAL)
        expect(modal_locator).to_be_visible()
        expect(modal_locator).to_contain_text(self.CHECK_INCORRECT_FORMAT_FILE_TEXT)
        self.upload_document(page, self.DOCUMENT_TYPE,
                             [self.PATH_TO_OVERSIZE_FILE])
        expect(modal_locator).to_be_visible()
        expect(modal_locator).to_contain_text(self.CHECK_OVERSIZE_FILE)

    def test_format_upload_file(self, page: Page):
        self.navigate_to_new_questionnaire(page)
        self.upload_document(page, self.DOCUMENT_TYPE,
                             [self.PATH_TO_FIRST_OK_FILE, self.PATH_TO_SECOND_OK_FILE])
        with page.expect_popup() as new_page_info:
            page.click(f'[data-label="{self.DOCUMENT_TYPE}"]')
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        expect(new_page).to_have_url(re.compile(r'.*\.pdf$'))
        assert new_page.url.endswith('.pdf'), f"URL does not end with '.pdf': {new_page.url}"

    def show_partner_offers(self, page, fin_term):
        page.select_option(self.FINANCING_TERM_SELECTOR, fin_term)
        page.wait_for_timeout(1000)
        page.click(self.SHOW_PARTNER_OFFERS_BUTTON)
        container = page.locator(self.OFFERS_CONTAINER_SELECTOR)
        expect(container).not_to_be_empty()

    def navigate_to_new_questionnaire(self, page: Page):
        page.wait_for_selector(self.NEW_QUESTIONNAIRE_ICON)
        page.hover(self.NEW_QUESTIONNAIRE_ICON)
        page.get_by_test_id(self.NEW_QUESTIONNAIRE_BUTTON).click()
        expect(page).to_have_url(re.compile(rf'{BASE_URL}/credit/car-form/\d+/'))

    def upload_document(self, page: Page, document_type: str, files):
        page.wait_for_timeout(1000)
        if not page.is_visible(self.DOCUMENT_TYPE_SELECT):
            page.click(self.COLLAPSE_DOCUMENTS_BUTTON)
        page.select_option(self.DOCUMENT_TYPE_SELECT, document_type)
        page.set_input_files(self.FILE_INPUT, files)
        page.get_by_test_id(self.UPLOAD_DOCS_BUTTON).click()
        page.wait_for_selector(self.ALERT_MODAL, state='visible')
        page.click(self.ALERT_MODAL_CLOSE_BUTTON)

    def delete_doc(self, page: Page):
        document_div = page.locator(self.UPLOAD_FILE_CLIENT + ' div',
                                    has=page.locator('a', has_text=self.DOCUMENT_TYPE))
        delete_button = document_div.locator(self.DELETE_DOC_BUTTON)
        delete_button.click()
        page.wait_for_selector(self.DELETE_MODAL_LABEL, state='visible')
        page.click(self.DELETE_CONFIRM_BUTTON)

        # Проверка, что документ удален в нужном блоке
        expect(page.locator(self.ACCORDION_UPLOADED_DOCUMENTS + ' ' + self.UPLOAD_FILE_CLIENT)).not_to_have_text(
            self.DOCUMENT_TYPE)
