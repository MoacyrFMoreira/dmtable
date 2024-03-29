# Generated by Django 3.1.3 on 2021-07-05 20:16

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gametable', '0002_delete_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.CharField(max_length=255, verbose_name='Nome da Campanha')),
                ('day', models.DateField(verbose_name='Dia')),
                ('time', models.TimeField(verbose_name='Hora')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='campaign', unique=True)),
                ('notes', models.TextField(blank=True, verbose_name='Notas Gerais')),
                ('dm_only', models.TextField(blank=True, verbose_name='Notas do Mestre')),
                ('moon', models.CharField(choices=[('1', 'Lua Nova'), ('2', 'Lua Crescente Crescente'), ('3', 'Meia Lua Crescente'), ('4', 'Lua Gibosa Crescente'), ('5', 'Lua Cheia'), ('6', 'Lua Gibosa Minguante'), ('7', 'Meia Lua Minguante'), ('8', 'Lua Crescente Minguante')], max_length=1, verbose_name='Lua')),
                ('moon_day', models.PositiveIntegerField(verbose_name='Dia da Lua')),
            ],
        ),
    ]
