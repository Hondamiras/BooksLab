# Generated by Django 5.1.4 on 2024-12-15 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_usersmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersmodel',
            name='image',
        ),
    ]
