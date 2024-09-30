import os

import boto3
from botocore.client import Config
import requests

# Настройки для работы с Yandex S3
ACCESS_KEY = os.getenv('UNISENDER_API_KEY')
SECRET_KEY = os.getenv('UNISENDER_API_KEY')
ENDPOINT_URL = 'https://storage.yandexcloud.net'

s3_client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    endpoint_url=ENDPOINT_URL,
    config=Config(signature_version='s3v4')
)


def get_s3_data(bucket_name, destination_blob_name=None):
    """Получение объекта из S3"""
    return s3_client.get_object(Bucket=bucket_name, Key=destination_blob_name)


def generate_signed_url(bucket_name, destination_blob_name, expiration=900):
    """Генерация подписанного URL для сканов документов (900 секунд = 15 минут)"""
    url = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': destination_blob_name},
        ExpiresIn=expiration
    )
    return url


def upload_to_bucket(bucket_name, file_content, destination_blob_name):
    """Загрузка скана в бакет"""
    s3_client.put_object(Bucket=bucket_name, Key=destination_blob_name, Body=file_content)
    print(f"File uploaded to {destination_blob_name}.")


def delete_from_bucket(bucket_name, destination_blob_name):
    """Удаление файла из бакета"""
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=destination_blob_name)
        print(f"Blob {destination_blob_name} deleted.")
    except Exception as e:
        print(f"Error deleting blob: {e}")


def send_file_directly_from_bucket(api_url, bucket_name, destination_blob_name):
    """Отправляет файл напрямую из S3 по API"""
    blob_data = get_s3_data(bucket_name, destination_blob_name)['Body'].read()

    files = {'file': (destination_blob_name, blob_data)}
    response = requests.post(api_url, files=files)
    return response


def delete_folder(bucket_name, folder_name):
    """Удаление папки из бакета (удаление всех объектов с указанным префиксом)"""
    objects_to_delete = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)

    if 'Contents' in objects_to_delete:
        for obj in objects_to_delete['Contents']:
            s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
            print(f"Blob {obj['Key']} deleted.")
