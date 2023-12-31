# Generated by Django 3.2 on 2021-10-13 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0010_auto_20211012_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='sankalp_skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('umedwar_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('second_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('fa_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('birth_date', models.DateField(blank=True, default=None, null=True)),
                ('paripurn_patta', models.CharField(blank=True, max_length=1000, null=True)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('email_id', models.EmailField(default=None, max_length=254)),
                ('gender', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('education', models.CharField(blank=True, max_length=1000, null=True)),
                ('adhaar_no', models.CharField(blank=True, max_length=100, null=True)),
                ('shakha', models.CharField(blank=True, max_length=100, null=True)),
                ('dharma', models.CharField(blank=True, max_length=100, null=True)),
                ('jat', models.CharField(blank=True, max_length=100, null=True)),
                ('pravarg', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('rahivasi', models.BooleanField(blank=True, default=None, null=True)),
                ('prashikshan', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('course_prashikshan', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('kau_prashikshan', models.BooleanField(blank=True, default=None, null=True)),
                ('vikas_prashikshan', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('magas', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('signature', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('scheme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schememodel')),
                ('scheme_register', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schemeregistrationmodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sankalp_skill',
            },
        ),
    ]
