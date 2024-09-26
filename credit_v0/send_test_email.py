import requests

UNISENDER_API_KEY = '6u53p7tbymwsyoz4ckipsy1udsqid6gt4ydpby8e'
LIST_ID = '1'  # Замените на ваш действительный идентификатор списка
recipient_email = 'faiver90@mail.ru'


def send_email_via_unisender(subject, content):
    url = "https://api.unisender.com/ru/api/sendEmail?format=json"
    payload = {
        'api_key': UNISENDER_API_KEY,
        'email': recipient_email,
        'sender_name': 'YourName',
        'sender_email': 'faiver90@gmail.com',
        'subject': subject,
        'body': content,
        'list_id': LIST_ID,
    }
    response = requests.post(url, data=payload)
    print(f"Status code: {response.status_code}")
    print("Response content:", response.json())


if __name__ == "__main__":
    subject = "Test Email"
    content = "This is a test email sent via Unisender API."

    send_email_via_unisender(subject, content)
