# Generated by Django 3.2 on 2021-10-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0004_auto_20211011_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ramai_gharkul',
            name='photo',
            field=models.FileField(blank=True, default=None, null=True, upload_to='media'),
        ),
    ]