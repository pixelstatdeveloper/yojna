# Generated by Django 3.2.4 on 2022-04-27 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0076_anusuchit_janavare_anusuchit_shelya'),
    ]

    operations = [
        migrations.CreateModel(
            name='thakkar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('san', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('gp_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('tbarea_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('paripurn_patta', models.CharField(blank=True, max_length=1000, null=True)),
                ('total_population', models.IntegerField(blank=True, default=None, null=True)),
                ('anusuchit_population', models.IntegerField(blank=True, default=None, null=True)),
                ('living_castes', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('prastav_bandhkam', models.CharField(blank=True, default=None, max_length=3000, null=True)),
                ('bfor_anudan', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('anudan_amount', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('gp_xtranudan', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('gp_sixmonth', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('talathi_satbara', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('gp_shilak', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('sachivsign', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('sarpanchsign', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('scheme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schememodel')),
                ('scheme_register', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schemeregistrationmodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'thakkar',
            },
        ),
    ]