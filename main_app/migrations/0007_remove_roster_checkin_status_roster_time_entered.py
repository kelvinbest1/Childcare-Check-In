# Generated by Django 4.2 on 2023-04-19 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_roster_checkin_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roster',
            name='checkin_status',
        ),
        migrations.AddField(
            model_name='roster',
            name='time_entered',
            field=models.TimeField(default='8:30'),
        ),
    ]
