# Generated by Django 4.1 on 2022-08-05 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_remove_doctor_users_doctor_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='users',
            new_name='user',
        ),
    ]
