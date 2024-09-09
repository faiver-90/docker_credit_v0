import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from gunicorn.config import User


class PasswordResetService:
    User = get_user_model()

    @staticmethod
    def generate_reset_context(user, domain, is_secure):
        """Генерация контекста для email сброса пароля"""
        return {
            'email': user.email,
            'domain': domain,
            'site_name': 'MySite',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
            'token': default_token_generator.make_token(user),
            'protocol': 'https' if is_secure else 'http',
        }


    def send_password_reset_email(self,user_email, domain, is_secure, subject_template_name, email_template_name):
        """Отправка email для сброса пароля через Unisender API"""
        try:
            user = self.User.objects.get(email=user_email)
        except self.User.DoesNotExist:
            return {'status': 'error', 'message': 'Пользователь с указанным адресом электронной почты не найден.'}

        # Генерация контекста и шаблонов для письма
        context = PasswordResetService.generate_reset_context(user, domain, is_secure)
        subject = render_to_string(subject_template_name, context).replace("\n", "")
        body = render_to_string(email_template_name, context)

        # Отправка email через Unisender API
        payload = {
            'api_key': settings.UNISENDER_API_KEY,
            'email': user_email,
            'sender_name': 'Motor Finance',
            'sender_email': settings.DEFAULT_FROM_EMAIL,
            'subject': subject,
            'body': body,
            'list_id': settings.UNISENDER_LIST_ID,
        }

        response = requests.post("https://api.unisender.com/ru/api/sendEmail?format=json", data=payload)

        if response.status_code == 200:
            return {'status': 'success', 'message': 'Письмо отправлено успешно.'}
        else:
            return {'status': 'error', 'message': f"Ошибка при отправке письма: {response.json()}"}
