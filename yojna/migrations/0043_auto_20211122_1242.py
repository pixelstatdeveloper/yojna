# Generated by Django 3.2 on 2021-11-22 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0042_auto_20211122_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='pramod_mah',
            name='course_prashikshan1',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='pramod_mah',
            name='course_prashikshan2',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='pramod_mah',
            name='prashikshan1',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='pramod_mah',
            name='prashikshan2',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]
