# Generated by Django 4.1 on 2022-08-05 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_user_doctor_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]