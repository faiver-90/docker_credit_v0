# Generated by Django 5.1 on 2024-10-07 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_event_user_id_alter_event_aggregate_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='user_id',
            new_name='id_user_changing',
        ),
    ]
