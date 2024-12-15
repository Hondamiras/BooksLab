# Generated by Django 5.1.4 on 2024-12-15 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0002_bookmodel_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmodel',
            old_name='genre',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]