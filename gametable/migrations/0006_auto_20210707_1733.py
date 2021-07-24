# Generated by Django 3.1.3 on 2021-07-07 20:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gametable', '0005_auto_20210705_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='day',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Dia'),
        ),
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='game',
            name='moon',
            field=models.CharField(choices=[('1', 'Lua Nova'), ('2', 'Lua Crescente Crescente'), ('3', 'Meia Lua Crescente'), ('4', 'Lua Gibosa Crescente'), ('5', 'Lua Cheia'), ('6', 'Lua Gibosa Minguante'), ('7', 'Meia Lua Minguante'), ('8', 'Lua Crescente Minguante')], default='5', max_length=1, verbose_name='Lua'),
        ),
        migrations.AlterField(
            model_name='game',
            name='moon_day',
            field=models.PositiveIntegerField(default=1, verbose_name='Dia da Lua'),
        ),
        migrations.AlterField(
            model_name='game',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Hora'),
        ),
    ]