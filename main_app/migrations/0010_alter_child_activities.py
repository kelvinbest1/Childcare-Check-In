# Generated by Django 4.2 on 2023-04-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_child_activities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='activities',
            field=models.ManyToManyField(blank=True, to='main_app.activity'),
        ),
    ]
