# Generated by Django 3.2 on 2021-11-30 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0057_tsp_cycl'),
    ]

    operations = [
        migrations.AddField(
            model_name='swadhar_yoj',
            name='pot',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]