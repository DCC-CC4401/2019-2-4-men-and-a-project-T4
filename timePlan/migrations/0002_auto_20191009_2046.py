# Generated by Django 2.2.6 on 2019-10-09 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timePlan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='correo',
            field=models.EmailField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='perfilusuario',
            name='foto_perfil',
            field=models.ImageField(default='fotos/aceitunas.jpg', upload_to='fotos'),
        ),
    ]
