# Generated by Django 4.2.6 on 2023-11-02 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_rename_caña_pesca_caña_de_pescar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('capacidad_en_metros', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Señuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30)),
                ('anzuelos', models.IntegerField()),
                ('color', models.TextField()),
            ],
        ),
    ]
