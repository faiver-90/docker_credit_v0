from django.test import TestCase

from credit_v0.forms.car_application_form import *


class FormValidationTests(TestCase):

    def test_PreDataClientForm_valid(self):
        form_data = {
            'first_name_to_contact_pre_client': 'Иван',
            'type_pre_client': 'Физическое лицо',
            'product_pre_client': 'Автокредит',
            'phone_number_pre_client': '+7 (123) 456-78-90',
            'type_phone_pre_client': 'Мобильный',
        }
        form = PreDataClientForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_PreDataClientForm_invalid(self):
        form_data = {
            'first_name_to_contact_pre_client': '',
            'type_pre_client': 'Физическое лицо',
            'product_pre_client': 'Автокредит',
            'phone_number_pre_client': '12345',
            'type_phone_pre_client': 'Мобильный',
        }
        form = PreDataClientForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name_to_contact_pre_client', form.errors)
        self.assertIn('phone_number_pre_client', form.errors)

    def test_CarInfoForm_valid(self):
        form_data = {
            'brand_car_info': 'Toyota',
            'model_car_info': 'Corolla',
            'condition_car_info': 'Новое',
            'configuration_car_info': 'Базовая',
            'year_car_info': '2021',
            'engine_volume_car_info': '1.8',
            'power_car_info': '140',
            'color_car_info': 'Белый',
            'mileage_car_info': '10000',
            'engine_type_car_info': 'Бензин',
            'vin_car_info': '1HGBH41JXMN109186',
            'car_price_car_info': '1500000',
            'dealer_equipment_price_car_info': '50000',
        }
        form = CarInfoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_CarInfoForm_invalid(self):
        form_data = {
            'brand_car_info': '',
            'model_car_info': '',
            'condition_car_info': 'Новое',
            'configuration_car_info': 'Базовая',
            'year_car_info': 'abcd',
            'engine_volume_car_info': '1.8',
            'power_car_info': '140',
            'color_car_info': 'Белый',
            'mileage_car_info': '-10000',
            'engine_type_car_info': 'Бензин',
            'vin_car_info': '1HGBH41JXMN109186',
            'car_price_car_info': '-1500000',
            'dealer_equipment_price_car_info': '50000',
        }
        form = CarInfoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('brand_car_info', form.errors)
        self.assertIn('year_car_info', form.errors)
        self.assertIn('mileage_car_info', form.errors)
        self.assertIn('car_price_car_info', form.errors)
