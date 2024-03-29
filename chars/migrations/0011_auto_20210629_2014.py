# Generated by Django 3.1.3 on 2021-06-29 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chars', '0010_auto_20210629_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='allies',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='ancestors',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='contacts',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='fate',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='fetish',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='kinfolk',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='mentor',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='pack_status',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='prestige',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='pure_breed',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='resources',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='rites',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='spirit_heritage',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='spirit_network',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='totem',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='academics',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='alertness',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='animal_ken',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='appearance',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='athletics',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='brawl',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='charisma',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='computer',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='crafts',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='dextery',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='drive',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='empathy',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='enigmas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='etiquette',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='expression',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='firearms',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='intelligence',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='intimidation',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='investigation',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='larceny',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='law',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='leadership',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='manipulation',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='medicine',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='melee',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='occult',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='perception',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='performance',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='primal_urge',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='rituals',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='science',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='stamina',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='stealth',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='streetwise',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='strength',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='subterfuge',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='survival',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='technology',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='wits',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
