# Generated by Django 3.1.3 on 2021-06-26 06:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 26, 3, 30, 16, 636523)),
        ),
        migrations.AlterField(
            model_name='post',
            name='dm_only',
            field=models.TextField(blank=True, null=True),
        ),
    ]
