# Generated by Django 4.2 on 2023-04-22 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0013_alter_activity_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roster',
            name='user',
        ),
        migrations.AddField(
            model_name='child',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
