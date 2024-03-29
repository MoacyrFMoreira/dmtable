# Generated by Django 3.1.3 on 2021-06-29 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chars', '0006_auto_20210629_1819'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rank',
            options={'ordering': ('bonus',)},
        ),
        migrations.AddField(
            model_name='character',
            name='auspice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chars.auspice'),
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chars.race'),
        ),
        migrations.AddField(
            model_name='character',
            name='rank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chars.rank'),
        ),
        migrations.AddField(
            model_name='character',
            name='tribe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chars.tribe'),
        ),
    ]
