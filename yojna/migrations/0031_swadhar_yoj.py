# Generated by Django 3.2 on 2021-10-25 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0030_gayakvad'),
    ]

    operations = [
        migrations.CreateModel(
            name='swadhar_yoj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('end_date1', models.DateField(blank=True, default=None, null=True)),
                ('arjname', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('mob_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('adhar', models.IntegerField(blank=True, default=None, null=True)),
                ('signature1', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('photo', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('sur_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('fa_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('name1', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('sur_name1', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('fa_name1', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('hus_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('mo_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('pravarg', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('ghar_kr', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('rasta', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('khun', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('gav', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('taluka', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('jilha', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pin', models.IntegerField(blank=True, default=None, null=True)),
                ('praman', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('dakhla_date', models.DateField(blank=True, default=None, null=True)),
                ('karya_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('divyang', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('jilha_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('praman1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('jari_date', models.DateField(blank=True, default=None, null=True)),
                ('jat', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('gav1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('taluka1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('jilha1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('adhar_card_no', models.IntegerField(blank=True, default=None, null=True)),
                ('adhar_patta', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('bank_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('shakha', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('acc_no', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('ifsc', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('purava', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('maha_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('maha_patta', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('idno', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('abhyas_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('year', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pravesh_date', models.DateField(blank=True, default=None, null=True)),
                ('kalavadhi', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('graduation', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pravesh_date1', models.DateField(blank=True, default=None, null=True)),
                ('uttirna', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('ekun_gun', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('prapta_gun', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('takka', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pravesh_date2', models.DateField(blank=True, default=None, null=True)),
                ('uttirna1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('ekun_gun1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('prapta_gun1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('takka1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pravesh_date3', models.DateField(blank=True, default=None, null=True)),
                ('uttirna2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('ekun_gun2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('prapta_gun2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('takka2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('fee', models.BooleanField(blank=True, default=None, null=True)),
                ('userid', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('palak_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('nate', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('mrutyu_purava', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('business', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('business_patta', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('income_cer', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('income', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('income_yr', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('place', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('end_date', models.DateField(blank=True, default=None, null=True)),
                ('sakshi1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('sakshi2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('sakshi1_sign', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('sakshi2_sign', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('signature', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('scheme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schememodel')),
                ('scheme_register', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schemeregistrationmodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'swadhar_yoj',
            },
        ),
    ]
