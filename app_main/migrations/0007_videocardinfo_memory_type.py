# Generated by Django 4.1.3 on 2023-01-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0006_remove_videocardinfo_cooling_width_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocardinfo',
            name='memory_type',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
