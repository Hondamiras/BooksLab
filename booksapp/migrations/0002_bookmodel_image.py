# Generated by Django 5.1.4 on 2024-12-15 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='books/'),
        ),
    ]
