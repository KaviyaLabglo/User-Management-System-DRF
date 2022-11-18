# Generated by Django 4.0 on 2022-11-18 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('myapp', '0005_delete_usermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('about_me', models.TextField(blank=True, default='', max_length=10000)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other'), ('not specified', 'Not specified')], default='not specified', max_length=32)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='accounts/users/profile-pictures')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
