# Generated by Django 5.1 on 2024-10-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0010_alter_clientpredata_product_pre_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientpredata',
            name='product_pre_client',
            field=models.CharField(blank=True, default='Кредит на автомобиль', max_length=255, null=True, verbose_name='Продукт'),
        ),
    ]
