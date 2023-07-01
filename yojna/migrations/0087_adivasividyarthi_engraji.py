# Generated by Django 3.2.4 on 2022-05-09 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0086_anusuchit_scholar'),
    ]

    operations = [
        migrations.CreateModel(
            name='adivasividyarthi_engraji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std1', models.CharField(blank=True, default=None, max_length=2, null=True)),
                ('std2', models.CharField(blank=True, default=None, max_length=2, null=True)),
                ('name', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('birth_date', models.DateField(blank=True, default=None, null=True)),
                ('birth_place', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('jamat', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('nation', models.CharField(blank=True, default=None, max_length=25, null=True)),
                ('rahivasi_yn', models.CharField(blank=True, default=None, max_length=4, null=True)),
                ('rahivasi', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('father_name', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('current_add', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('kayam_add', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('mobile1', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True)),
                ('mobile2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True)),
                ('mother_name', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('income_cf', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('vyavsay', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('nokardar_cf', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('daridrya_cf', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('mahilapalak_cf', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('sign', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('photo', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('scheme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schememodel')),
                ('scheme_register', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schemeregistrationmodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'adivasividyarthi_engraji',
            },
        ),
    ]