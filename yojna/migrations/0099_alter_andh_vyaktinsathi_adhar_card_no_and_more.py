# Generated by Django 4.1 on 2022-11-24 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0098_usermodel_subdepartment_rajarshi_shahuscholar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='andh_vyaktinsathi',
            name='adhar_card_no',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='swadhar_yoj',
            name='adhar',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='swadhar_yoj',
            name='adhar_card_no',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
       
    ]