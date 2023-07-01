# Generated by Django 3.2.4 on 2022-06-14 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0094_shubhmangal_nondni_silk_samagra'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='rajarshi_shahuscholar',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('name', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('edu_type', models.CharField(blank=True, default=None, max_length=3, null=True)),
        #         ('edu_branch', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('other_edu', models.CharField(blank=True, default=None, max_length=20, null=True)),
        #         ('address', models.CharField(blank=True, default=None, max_length=150, null=True)),
        #         ('mob_no', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
        #         ('jat', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('birthdate_ank', models.DateField(blank=True, default=None, null=True)),
        #         ('birthdate_akshar', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('age', models.CharField(blank=True, default=None, max_length=2, null=True)),
        #         ('email_id', models.EmailField(default=None, max_length=254)),
        #         ('adhar_no', models.BigIntegerField(blank=True, default=None, null=True)),
        #         ('adhar_prat', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
        #         ('pan_no', models.CharField(blank=True, default=None, max_length=20, null=True)),
        #         ('mahavasi_yn', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('ssc_abhyaskram', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('ssc_passyear', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('ssc_institute', models.CharField(blank=True, default=None, max_length=120, null=True)),
        #         ('ssc_totalmarks', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('ssc_obtainmarks', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('ssc_takke', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('hsc_abhyaskram', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('hsc_passyear', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('hsc_institute', models.CharField(blank=True, default=None, max_length=120, null=True)),
        #         ('hsc_totalmarks', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('hsc_obtainmarks', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('hsc_takke', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('padvi_abhyaskram', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('padvi_passyear', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('padvi_institute', models.CharField(blank=True, default=None, max_length=120, null=True)),
        #         ('padvi_totalmarks', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('padvi_obtainmarks', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('padvi_takke', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('padvika_abhyaskram', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('padvika_passyear', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('padvika_institute', models.CharField(blank=True, default=None, max_length=120, null=True)),
        #         ('padvika_totalmarks', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('padvika_obtainmarks', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('padvika_takke', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('gre_abhyaskram', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('gre_passyear', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('gre_institute', models.CharField(blank=True, default=None, max_length=120, null=True)),
        #         ('gre_totalmarks', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('gre_obtainmarks', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('gre_takke', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('toefl_abhyaskram', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('toefl_passyear', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('toefl_institute', models.CharField(blank=True, default=None, max_length=120, null=True)),
        #         ('toefl_totalmarks', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('toefl_obtainmarks', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('toefl_takke', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('vyavsay', models.CharField(blank=True, default=None, max_length=80, null=True)),
        #         ('naukri', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('hudda', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('vn_income', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('inc_cf', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
        #         ('noc_yn', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('karyalay', models.CharField(blank=True, default=None, max_length=80, null=True)),
        #         ('office_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
        #         ('office_email', models.EmailField(default=None, max_length=254)),
        #         ('married', models.CharField(blank=True, default=None, max_length=8, null=True)),
        #         ('husband_wifename', models.CharField(blank=True, default=None, max_length=80, null=True)),
        #         ('child1', models.CharField(blank=True, default=None, max_length=80, null=True)),
        #         ('child2', models.CharField(blank=True, default=None, max_length=80, null=True)),
        #         ('sobat_yn', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('acholder_nm', models.CharField(blank=True, default=None, max_length=80, null=True)),
        #         ('bank_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('branch', models.CharField(blank=True, default=None, max_length=30, null=True)),
        #         ('acc_no', models.BigIntegerField(blank=True, default=None, null=True)),
        #         ('ifsc', models.CharField(blank=True, default=None, max_length=30, null=True)),
        #         ('micr', models.CharField(blank=True, default=None, max_length=40, null=True)),
        #         ('passport_no', models.CharField(blank=True, default=None, max_length=30, null=True)),
        #         ('issue_date', models.DateField(blank=True, default=None, null=True)),
        #         ('end_date', models.DateField(blank=True, default=None, null=True)),
        #         ('offerletter_no', models.CharField(blank=True, default=None, max_length=30, null=True)),
        #         ('offerletter_date', models.DateField(blank=True, default=None, null=True)),
        #         ('at_vinaat', models.CharField(blank=True, default=None, max_length=8, null=True)),
        #         ('konti_at', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('abyaskram', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('labh_yn', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('year', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('sanstha', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('abhyaskram_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('abhyaskram_validity', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('shishyavrutti', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('palak_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('palak_address', models.CharField(blank=True, default=None, max_length=150, null=True)),
        #         ('palak_mob', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
        #         ('palak_email', models.EmailField(default=None, max_length=254)),
        #         ('palak_vyavsay', models.CharField(blank=True, default=None, max_length=80, null=True)),
        #         ('palak_naukri', models.CharField(blank=True, default=None, max_length=120, null=True)),
        #         ('palak_hudda', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('palak_income', models.CharField(blank=True, default=None, max_length=15, null=True)),
        #         ('palakincome_cf', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
        #         ('palak_officeadd', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('palakoffice_mob', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
        #         ('palakoffice_email', models.EmailField(default=None, max_length=254)),
        #         ('yearly_income', models.CharField(blank=True, default=None, max_length=15, null=True)),
        #         ('yearincome_yn', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('yearincome_cf', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
        #         ('tax', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('tax_yn', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('tax_cf', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
        #         ('vadil_yn', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('vadil_cf', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
        #         ('nyayalay', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('nyayalay_cf', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
        #         ('sampurn_nav1', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('age1', models.CharField(blank=True, default=None, max_length=2, null=True)),
        #         ('vyavsay1', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('income1', models.CharField(blank=True, default=None, max_length=15, null=True)),
        #         ('scholar_yn1', models.CharField(blank=True, default=None, max_length=20, null=True)),
        #         ('sampurn_nav2', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('age2', models.CharField(blank=True, default=None, max_length=2, null=True)),
        #         ('nate2', models.CharField(blank=True, default=None, max_length=30, null=True)),
        #         ('vyavsay2', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('income2', models.CharField(blank=True, default=None, max_length=15, null=True)),
        #         ('scholar_yn2', models.CharField(blank=True, default=None, max_length=20, null=True)),
        #         ('sampurn_nav3', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('age3', models.CharField(blank=True, default=None, max_length=2, null=True)),
        #         ('nate3', models.CharField(blank=True, default=None, max_length=30, null=True)),
        #         ('vyavsay3', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('income3', models.CharField(blank=True, default=None, max_length=15, null=True)),
        #         ('scholar_yn3', models.CharField(blank=True, default=None, max_length=20, null=True)),
        #         ('sampurn_nav4', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('age4', models.CharField(blank=True, default=None, max_length=2, null=True)),
        #         ('nate4', models.CharField(blank=True, default=None, max_length=30, null=True)),
        #         ('vyavsay4', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('income4', models.CharField(blank=True, default=None, max_length=15, null=True)),
        #         ('scholar_yn4', models.CharField(blank=True, default=None, max_length=20, null=True)),
        #         ('sampurn_nav5', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('age5', models.CharField(blank=True, default=None, max_length=2, null=True)),
        #         ('nate5', models.CharField(blank=True, default=None, max_length=30, null=True)),
        #         ('vyavsay5', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('income5', models.CharField(blank=True, default=None, max_length=15, null=True)),
        #         ('scholar_yn5', models.CharField(blank=True, default=None, max_length=20, null=True)),
        #         ('sampurn_nav6', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('age6', models.CharField(blank=True, default=None, max_length=2, null=True)),
        #         ('nate6', models.CharField(blank=True, default=None, max_length=30, null=True)),
        #         ('vyavsay6', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('income6', models.CharField(blank=True, default=None, max_length=15, null=True)),
        #         ('scholar_yn6', models.CharField(blank=True, default=None, max_length=20, null=True)),
        #         ('sampurn_nav7', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('age7', models.CharField(blank=True, default=None, max_length=2, null=True)),
        #         ('nate7', models.CharField(blank=True, default=None, max_length=30, null=True)),
        #         ('vyavsay7', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('income7', models.CharField(blank=True, default=None, max_length=15, null=True)),
        #         ('scholar_yn7', models.CharField(blank=True, default=None, max_length=20, null=True)),
        #         ('sampurn_nav8', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('age8', models.CharField(blank=True, default=None, max_length=2, null=True)),
        #         ('nate8', models.CharField(blank=True, default=None, max_length=30, null=True)),
        #         ('vyavsay8', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('income8', models.CharField(blank=True, default=None, max_length=15, null=True)),
        #         ('scholar_yn8', models.CharField(blank=True, default=None, max_length=20, null=True)),
        #         ('sampurn_nav9', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('age9', models.CharField(blank=True, default=None, max_length=2, null=True)),
        #         ('nate9', models.CharField(blank=True, default=None, max_length=30, null=True)),
        #         ('vyavsay9', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('income9', models.CharField(blank=True, default=None, max_length=15, null=True)),
        #         ('scholar_yn9', models.CharField(blank=True, default=None, max_length=20, null=True)),
        #         ('sampurn_nav10', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('age10', models.CharField(blank=True, default=None, max_length=2, null=True)),
        #         ('nate10', models.CharField(blank=True, default=None, max_length=30, null=True)),
        #         ('vyavsay10', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('income10', models.CharField(blank=True, default=None, max_length=15, null=True)),
        #         ('scholar_yn10', models.CharField(blank=True, default=None, max_length=20, null=True)),
        #         ('kutumb_income', models.CharField(blank=True, default=None, max_length=15, null=True)),
        #         ('pravesh_varsh', models.CharField(blank=True, default=None, max_length=4, null=True)),
        #         ('vidyapith', models.CharField(blank=True, default=None, max_length=150, null=True)),
        #         ('desh', models.CharField(blank=True, default=None, max_length=30, null=True)),
        #         ('shasan', models.CharField(blank=True, default=None, max_length=30, null=True)),
        #         ('vidyapith_name', models.CharField(blank=True, default=None, max_length=150, null=True)),
        #         ('qsworld_rank', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('vidyarthi_abhyas', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('abhyas_swarup', models.CharField(blank=True, default=None, max_length=10, null=True)),
        #         ('kalavadhi', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('pravesh_dinank', models.DateField(blank=True, default=None, null=True)),
        #         ('pardesh_patta', models.CharField(blank=True, default=None, max_length=120, null=True)),
        #         ('pardesh_mob', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
        #         ('pardesh_email', models.EmailField(default=None, max_length=254)),
        #         ('shikshan1', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('shikshan2', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('shikshan3', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('shikshan4', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('pariksha1', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('pariksha2', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('pariksha3', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('pariksha4', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('nondni1', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('nondni2', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('nondni3', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('nondni4', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('jevan_rahne1', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('jevan_rahne2', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('jevan_rahne3', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('jevan_rahne4', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('vima1', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('vima2', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('vima3', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('vima4', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('other1', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('other2', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('other3', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('other4', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('total1', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('total2', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('total3', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('total4', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('other_scholar', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('fellowship', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('gtas', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('other_mandhan', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('campus', models.CharField(blank=True, default=None, max_length=100, null=True)),
        #         ('thikan', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('palak_sign', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
        #         ('vidyarthi_sign', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
        #         ('dinank', models.DateField(blank=True, default=None, null=True)),
        #         ('palak_nav', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('vidyarthi_nav', models.CharField(blank=True, default=None, max_length=50, null=True)),
        #         ('scheme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schememodel')),
        #         ('scheme_register', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schemeregistrationmodel')),
        #         ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
        #     ],
        #     options={
        #         'db_table': 'rajarshi_shahuscholar',
        #     },
        # ),
        migrations.CreateModel(
            name='mahatmagandhi_reshim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jilha', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('dinank', models.DateField(blank=True, default=None, null=True)),
                ('jilha2', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('yojna', models.CharField(blank=True, default=None, max_length=11, null=True)),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, default=None, max_length=8, null=True)),
                ('birthyear', models.CharField(blank=True, default=None, max_length=4, null=True)),
                ('jat', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('mukam', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('taluka', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('dist', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('mobile_no', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True)),
                ('adhar_no', models.BigIntegerField(blank=True, default=None, null=True)),
                ('education', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('bank_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('acc_no', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('branch', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('ifsc', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('land_type', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('gat_712', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('ekun_shetra', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('pik1', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('pik2', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('pik3', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('pik4', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('acre', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('sinchan_src', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('sinchan_time', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('vijjodni_yn', models.CharField(blank=True, default=None, max_length=4, null=True)),
                ('kitak_yn', models.CharField(blank=True, default=None, max_length=4, null=True)),
                ('majur_yn', models.CharField(blank=True, default=None, max_length=4, null=True)),
                ('shetkari_varg', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('daridrya_yn', models.CharField(blank=True, default=None, max_length=4, null=True)),
                ('bpl_no', models.CharField(blank=True, default=None, max_length=25, null=True)),
                ('ropvatika_yn', models.CharField(blank=True, default=None, max_length=4, null=True)),
                ('nam', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('padnam', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('karyalay', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('shetkari_sign', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('shetkari_name', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('scheme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schememodel')),
                ('scheme_register', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yojna.schemeregistrationmodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'mahatmagandhi_reshim',
            },
        ),
    ]
