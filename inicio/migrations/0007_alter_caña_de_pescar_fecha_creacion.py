# Generated by Django 4.2.6 on 2023-11-18 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_alter_caña_de_pescar_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caña_de_pescar',
            name='fecha_creacion',
            field=models.DateField(),
        ),
    ]
