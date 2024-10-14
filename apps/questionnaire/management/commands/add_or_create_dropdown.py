from django.apps import apps
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


class Command(BaseCommand):
    """
    Django команда для добавления или обновления значений выпадающих списков в базе данных.

    Эта команда предназначена для заполнения выпадающих списков (dropdown) различных моделей предопределёнными значениями.
    Команда проверяет, существует ли запись с указанным значением в заданной модели. Если запись не найдена, создаётся новая запись.

    Пример использования:

        $ python manage.py add_or_create_dropdown

    Значения для добавления задаются в словаре `data`, где ключ имеет формат `ModelName:field_name`,
    а значение — это список элементов, которые будут добавлены в соответствующее поле модели.

    Атрибуты:
        app_name (str): Название приложения, в котором находятся модели.
        data (dict): Словарь с данными для добавления в модели. Ключ — это название модели и поле, разделенные двоеточием,
                     значение — список элементов для добавления.
    Пример:
        data = {
            'Country:name': [
                'Россия',
                'США',
                'Германия',
                'Франция',
                'Китай'
            ]}
    """
    help = 'Add or update data in the database'
    app_name = 'questionnaire'
    data = {}

    def handle(self, *args, **kwargs):
        for model_field, values in self.data.items():
            model_name, field_name = model_field.split(':')
            Model = apps.get_model(self.app_name, model_name)
            # if model_name == 'CarCondition':
            #     # Удаляем все записи из таблицы
            #     Model.objects.all().delete()

            for value in values:
                try:
                    if not Model.objects.filter(**{field_name: value}).exists():
                        Model.objects.create(**{field_name: value})
                        self.stdout.write(self.style.SUCCESS(f'Created new entry: {value} in {model_name}'))
                    else:
                        self.stdout.write(f'Entry already exists: {value} in {model_name}')
                except IntegrityError as e:
                    self.stdout.write(self.style.ERROR(f'Error creating entry: {e}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error creating entry: {e}'))
