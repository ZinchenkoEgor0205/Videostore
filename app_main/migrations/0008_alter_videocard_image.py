# Generated by Django 4.1.3 on 2022-12-28 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0007_alter_videocard_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocard',
            name='image',
            field=models.FilePathField(path='videostore_project/media/', verbose_name='Изображение'),
        ),
    ]
