# Generated by Django 3.1.3 on 2021-07-02 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chars', '0021_auto_20210702_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.PositiveIntegerField(default=1)),
                ('type', models.CharField(choices=[('1', 'Menor'), ('2', 'Caern'), ('3', 'Místico'), ('4', 'Morte'), ('5', 'Pacto'), ('6', 'Periódico'), ('7', 'Punição'), ('8', 'Renome')], default='1', max_length=2)),
                ('system', models.TextField(blank=True)),
                ('efect', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='gift',
            options={'ordering': ('name',)},
        ),
    ]
