# Generated by Django 4.1.3 on 2022-12-29 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0014_remove_videocard_image_big_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videocard',
            name='image_upload',
        ),
    ]