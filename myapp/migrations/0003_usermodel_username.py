# Generated by Django 4.0 on 2022-11-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_usermodel_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='username',
            field=models.CharField(default=True, max_length=64),
            preserve_default=False,
        ),
    ]
