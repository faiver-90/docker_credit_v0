from django.test import TestCase, Client
from django.urls import reverse

from apps.questionnaire.models import *


class QuestionnaireViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = UserProfile.objects.create(user=self.user, first_name_manager='Test', last_name_manager='User')
        self.client.login(username='testuser', password='testpassword')

        self.pre_data_client = ClientPreData.objects.create(first_name_to_contact_pre_client='Test Client')
        self.extra_insurance = ClientExtraInsurance.objects.create(client=self.pre_data_client)
        self.financing_conditions = ClientFinancingCondition.objects.create(client=self.pre_data_client)
        self.car_info = ClientCarInfo.objects.create(client=self.pre_data_client)
        self.documents = AutoSaleDocument.objects.create(client=self.pre_data_client)
        self.application = AllApplications.objects.create(
            client=self.pre_data_client,
            financing_conditions=self.financing_conditions,
            car_info=self.car_info,
            documents=self.documents,
            extra_insurance=self.extra_insurance,
            status='Pending',
            type_all_app='Физическое лицо',
            financing='Кредит',
            manager='manager1',
            dealership_all_app='Dealership1',
            organization='Organization1'
        )
        self.questionnaire_url = reverse('car_form', kwargs={'pk': self.pre_data_client.pk})

    def test_questionnaire_view_get(self):
        response = self.client.get(self.questionnaire_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'questionnaire/car_form.html')

    def test_questionnaire_view_post(self):
        post_data = {
            'client_id': self.pre_data_client.id,
            'ignore_required': 'false',
            # добавьте все необходимые поля для успешного POST запроса
        }
        response = self.client.post(self.questionnaire_url, post_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'success')


class LoadAllDataClientViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = UserProfile.objects.create(user=self.user, first_name_manager='Test', last_name_manager='User')
        self.client.login(username='testuser', password='testpassword')

        self.pre_data_client = ClientPreData.objects.create(first_name_to_contact_pre_client='Test Client')
        self.extra_insurance = ClientExtraInsurance.objects.create(client=self.pre_data_client)
        self.financing_conditions = ClientFinancingCondition.objects.create(client=self.pre_data_client)
        self.car_info = ClientCarInfo.objects.create(client=self.pre_data_client)
        self.documents = AutoSaleDocument.objects.create(client=self.pre_data_client)
        self.load_all_data_url = reverse('load_all_data_client', kwargs={'pk': self.pre_data_client.pk})

    def test_load_all_data_client_view_get(self):
        response = self.client.get(self.load_all_data_url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'html')

    def test_load_all_data_client_view_post(self):
        post_data = {
            'ignore_required': 'false',
            # добавьте все необходимые поля для успешного POST запроса
        }
        response = self.client.post(self.load_all_data_url, post_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'success')


class CustomLoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = UserProfile.objects.create(user=self.user, first_name_manager='Test', last_name_manager='User')

    def test_login_page_renders_correctly(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_with_valid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_login_with_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password.")
