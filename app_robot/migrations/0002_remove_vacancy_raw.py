# Generated by Django 5.0.6 on 2024-07-05 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_robot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='raw',
        ),
    ]
