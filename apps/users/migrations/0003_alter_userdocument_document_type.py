# Generated by Django 5.1 on 2024-10-04 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userdocumenttype_userdocument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdocument',
            name='document_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.userdocumenttype', verbose_name='Тип документа'),
            preserve_default=False,
        ),
    ]
