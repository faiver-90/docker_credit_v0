# Generated by Django 5.1 on 2024-11-12 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0018_alter_selectedclientoffer_status_select_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='OffersSovComBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_excel_file_sovcom', models.IntegerField(blank=True, null=True, verbose_name='ID в ексель файле')),
                ('actual_sovcom', models.IntegerField(blank=True, null=True, verbose_name='actual столбец')),
                ('rating_sovcom', models.IntegerField(blank=True, null=True, verbose_name='Рейтинг выдачи')),
            ],
        ),
        migrations.CreateModel(
            name='ResponseAPICalculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.JSONField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.clientpredata')),
            ],
        ),
    ]