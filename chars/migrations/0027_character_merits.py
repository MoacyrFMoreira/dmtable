# Generated by Django 3.1.3 on 2021-07-03 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chars', '0026_merit'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='merits',
            field=models.ManyToManyField(blank=True, to='chars.Merit'),
        ),
    ]
