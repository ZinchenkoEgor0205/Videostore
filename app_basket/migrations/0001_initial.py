# Generated by Django 4.1.3 on 2023-01-07 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_main', '0007_videocardinfo_memory_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество')),
                ('add_datetime', models.DateTimeField(auto_now_add=True, verbose_name='время')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to=settings.AUTH_USER_MODEL)),
                ('videocard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_main.videocard')),
            ],
        ),
    ]
