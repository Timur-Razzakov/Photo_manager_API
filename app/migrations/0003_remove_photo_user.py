# Generated by Django 4.1.4 on 2022-12-14 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_authuser_alter_photo_user_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='user',
        ),
    ]