# Generated by Django 3.2.4 on 2022-05-09 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0085_antarjatiy_vivah'),
    ]

    operations = [
        migrations.CreateModel(
            name='anusuchit_scholar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('email_id', models.EmailField(default=None, max_length=254)),
                ('address', models.CharField(blank=True, default=None, max_length=140, null=True)),
                ('mob_no', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('jat', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('potjat', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('jat_cf', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('birthdate', models.DateField(blank=True, default=None, null=True)),
                ('birth_char', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('birth_cf', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('father_name', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('father_add', models.CharField(blank=True, default=None, max_length=140, null=True)),
                ('father_mob', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('father_email', models.EmailField(default=None, max_length=254)),
                ('busi_job', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('office_add', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('office_mob', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('office_email', models.EmailField(default=None, max_length=254)),
                ('income', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('income_cf', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('hsc_passyear', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('hsc_institute', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('hsc_marks', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('hsc_percent', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('ug_passyear', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('ug_institute', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('ug_marks', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('ug_percent', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('pg_passyear', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('pg_institute', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('pg_marks', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('pg_percent', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('name1', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('age1', models.CharField(blank=True, default=None, max_length=2, null=True)),
                ('nate1', models.CharField(blank=True, default=None, max_length=25, null=True)),
                ('business1', models.CharField(blank=True, default=None, max_length=35, null=True)),
                ('income1', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('name2', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('age2', models.CharField(blank=True, default=None, max_length=2, null=True)),
                ('nate2', models.CharField(blank=True, default=None, max_length=25, null=True)),
                ('business2', models.CharField(blank=True, default=None, max_length=35, null=True)),
                ('income2', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('name3', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('age3', models.CharField(blank=True, default=None, max_length=2, null=True)),
                ('nate3', models.CharField(blank=True, default=None, max_length=25, null=True)),
                ('business3', models.CharField(blank=True, default=None, max_length=35, null=True)),
                ('income3', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('name4', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('age4', models.CharField(blank=True, default=None, max_length=2, null=True)),
                ('nate4', models.CharField(blank=True, default=None, max_length=25, null=True)),
                ('business4', models.CharField(blank=True, default=None, max_length=35, null=True)),
                ('income4', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('name5', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('age5', models.CharField(blank=True, default=None, max_length=2, null=True)),
                ('nate5', models.CharField(blank=True, default=None, max_length=25, null=True)),
                ('business5', models.CharField(blank=True, default=None, max_length=35, null=True)),
                ('income5', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('abhyas', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('kalavadhi', models.CharField(blank=True, default=None, max_length=25, null=True)),
                ('intitute', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('university', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('college_add', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('college_mob', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True)),
                ('college_email', models.EmailField(default=None, max_length=254)),
                ('shikshan1', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('shikshan2', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('shikshan3', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('shikshan4', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('pariksha1', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('pariksha2', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('pariksha3', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('pariksha4', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('niwas1', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('niwas2', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('niwas3', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('niwas4', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('other1', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('other2', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('other3', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('other4', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('total1', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('total2', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('total3', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('total4', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('bank_name1', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('branch1', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('acc_no1', models.BigIntegerField(blank=True, default=None, null=True)),
                ('sortcode1', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('swiftcode1', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('ibpn_no1', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('bank_name2', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('branch2', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('acc_no2', models.BigIntegerField(blank=True, default=None, null=True)),
                ('sortcode2', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('swiftcode2', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('ibpn_no2', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('other_scholar', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('dinank', models.DateField(blank=True, default=None, null=True)),
                ('place', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('stu_nm', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('stu_sign', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('palak_nm', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('palak_sign', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('photo', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('scheme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schememodel')),
                ('scheme_register', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schemeregistrationmodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'anusuchit_scholar',
            },
        ),
    ]