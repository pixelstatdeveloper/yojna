# Generated by Django 3.2 on 2021-11-29 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0050_balsangopan'),
    ]

    operations = [
        migrations.CreateModel(
            name='shubh_vivah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('sam_patta', models.CharField(blank=True, max_length=1000, null=True)),
                ('post', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('taluka', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('buisness', models.CharField(blank=True, max_length=1000, null=True)),
                ('girl_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('age', models.CharField(blank=True, max_length=100, null=True)),
                ('vivah_date', models.DateField(blank=True, default=None, null=True)),
                ('sanstha', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('adhaar_no', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('acc_no', models.CharField(blank=True, max_length=100, null=True)),
                ('ifsc', models.CharField(blank=True, max_length=100, null=True)),
                ('name1', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('form_date', models.DateField(blank=True, default=None, null=True)),
                ('signature', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('var_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('age1', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_date', models.DateField(blank=True, default=None, null=True)),
                ('education', models.CharField(blank=True, max_length=1000, null=True)),
                ('gav', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('taluka1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('jilha', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('palak_patta', models.CharField(blank=True, max_length=1000, null=True)),
                ('mobile_number1', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('mobile_number2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('var_photo', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('vadhu_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('age2', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_date1', models.DateField(blank=True, default=None, null=True)),
                ('education1', models.CharField(blank=True, max_length=1000, null=True)),
                ('gav1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('taluka2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('jilha1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('mobile_number3', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('palak_patta1', models.CharField(blank=True, max_length=1000, null=True)),
                ('mobile_number4', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('mobile_number5', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('vadhu_photo', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('sans_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('thikan', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('tarikh', models.DateField(blank=True, default=None, null=True)),
                ('padhat', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('var', models.BooleanField(blank=True, default=None, null=True)),
                ('vadhu', models.BooleanField(blank=True, default=None, null=True)),
                ('vidhva', models.BooleanField(blank=True, default=None, null=True)),
                ('vidur', models.BooleanField(blank=True, default=None, null=True)),
                ('arthsahayya', models.BooleanField(blank=True, default=None, null=True)),
                ('arj', models.BooleanField(blank=True, default=None, null=True)),
                ('var_sign', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('vadhu_sign', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('scheme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schememodel')),
                ('scheme_register', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schemeregistrationmodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'shubh_vivah',
            },
        ),
    ]
