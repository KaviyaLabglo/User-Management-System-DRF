# Generated by Django 4.0 on 2022-11-18 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_usermodel_password2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
