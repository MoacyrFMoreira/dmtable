# Generated by Django 3.1.3 on 2021-07-09 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gametable', '0011_game_rolls'),
    ]

    operations = [
        migrations.AddField(
            model_name='battlechar',
            name='dice',
            field=models.IntegerField(default=0),
        ),
    ]
