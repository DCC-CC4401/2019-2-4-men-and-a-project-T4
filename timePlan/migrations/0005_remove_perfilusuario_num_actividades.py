# Generated by Django 2.2.6 on 2019-10-18 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timePlan', '0004_auto_20191018_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfilusuario',
            name='num_actividades',
        ),
    ]
