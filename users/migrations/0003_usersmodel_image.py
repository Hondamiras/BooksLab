# Generated by Django 5.1.4 on 2024-12-15 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usersmodel_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]