# Generated by Django 3.1.3 on 2021-06-29 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chars', '0007_auto_20210629_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='appearance',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='charisma',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='dextery',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='gnosis',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='intelligence',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='manipulation',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='perception',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='rage',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='stamina',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='strength',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='willpower',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='character',
            name='wits',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
    ]
