# Generated by Django 5.0.6 on 2024-07-12 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_robot', '0005_alter_vacancy_exp_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='building',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
