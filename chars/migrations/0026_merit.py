# Generated by Django 3.1.3 on 2021-07-03 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chars', '0025_auto_20210702_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('cost', models.IntegerField(blank=True, default=0)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
