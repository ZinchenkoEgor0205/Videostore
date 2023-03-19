# Generated by Django 4.1.3 on 2023-03-19 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0005_remove_profile_discount_status_profile_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='apartment',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='house',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='housing',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='street',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
