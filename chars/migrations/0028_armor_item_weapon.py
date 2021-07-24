# Generated by Django 3.1.3 on 2021-07-03 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chars', '0027_character_merits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('armor', models.IntegerField(default=1)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('dificulty', models.PositiveIntegerField(default=6)),
                ('damage', models.CharField(max_length=10)),
                ('range', models.CharField(blank=True, max_length=10)),
                ('bullets', models.CharField(blank=True, max_length=10)),
                ('stealth', models.CharField(blank=True, max_length=20)),
                ('attribute', models.CharField(choices=[('brawl', 'Briga'), ('melee', 'Armas Brancas'), ('firearms', 'Armas de Fogo'), ('athletics', 'Esportes')], default='brawl', max_length=10)),
                ('damage_type', models.CharField(choices=[('1', 'Contusão'), ('2', 'Letal'), ('3', 'Agravado')], default='2', max_length=1)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
