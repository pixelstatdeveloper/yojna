# Generated by Django 3.2 on 2021-11-29 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0052_otsp_shivnyantra'),
    ]

    operations = [
        migrations.CreateModel(
            name='scp_shivnyantra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('sam_patta', models.CharField(blank=True, max_length=1000, null=True)),
                ('mukkam', models.CharField(blank=True, max_length=1000, null=True)),
                ('post', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('taluka', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('birth_date', models.DateField(blank=True, default=None, null=True)),
                ('tc', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('jati', models.BooleanField(blank=True, default=None, null=True)),
                ('dakhla', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('jat', models.CharField(blank=True, max_length=100, null=True)),
                ('potjat', models.CharField(blank=True, max_length=100, null=True)),
                ('vivahit', models.CharField(blank=True, max_length=100, null=True)),
                ('patiname', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('buisness', models.CharField(blank=True, max_length=1000, null=True)),
                ('income', models.CharField(blank=True, max_length=100, null=True)),
                ('fa_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('buisness1', models.CharField(blank=True, max_length=1000, null=True)),
                ('income1', models.CharField(blank=True, max_length=100, null=True)),
                ('income2', models.CharField(blank=True, max_length=100, null=True)),
                ('dakhla1', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('buisness2', models.CharField(blank=True, max_length=1000, null=True)),
                ('income3', models.CharField(blank=True, max_length=100, null=True)),
                ('prashikshan', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('pramanpatra', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('prashikshan1', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('pramanpatra2', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('sthal', models.CharField(blank=True, max_length=100, null=True)),
                ('form_date', models.DateField(blank=True, default=None, null=True)),
                ('patta', models.CharField(blank=True, max_length=1000, null=True)),
                ('signature', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('photo', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('scheme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schememodel')),
                ('scheme_register', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schemeregistrationmodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'scp_shivnyantra',
            },
        ),
    ]
