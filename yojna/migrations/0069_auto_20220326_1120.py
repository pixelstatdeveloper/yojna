# Generated by Django 3.2 on 2022-03-26 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0068_auto_20220326_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navin_rashtriy',
            name='gas_sway',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='navin_rashtriy',
            name='sandas',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='navin_rashtriy',
            name='sanyantra',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='navin_rashtriy',
            name='shetmajur',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
