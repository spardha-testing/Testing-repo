# Generated by Django 3.2.12 on 2022-03-22 10:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0002_alter_team_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='captain_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='captain_phone',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
