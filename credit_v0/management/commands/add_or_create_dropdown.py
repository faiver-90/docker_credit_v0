from django.apps import apps
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Add or update data in the database'
    app_name = 'credit_v0'
    data = {
        # for example
        #    'CarMake:name': [
        #        'Ford',
        #        'Toyota',
        #        'BMW',
        #        'Geely'
        # ]
    }

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
