# Generated by Django 3.2 on 2021-10-25 09:42

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0033_auto_20211025_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gayakvad',
            old_name='hudda',
            new_name='adhi1',
        ),
        migrations.RenameField(
            model_name='gayakvad',
            old_name='birth_date',
            new_name='adhi1_date',
        ),
        migrations.RenameField(
            model_name='gayakvad',
            old_name='jat',
            new_name='adhi2',
        ),
        migrations.RenameField(
            model_name='gayakvad',
            old_name='form_date',
            new_name='adhi2_date',
        ),
        migrations.RenameField(
            model_name='gayakvad',
            old_name='pramanpatra',
            new_name='anubhav',
        ),
        migrations.RenameField(
            model_name='gayakvad',
            old_name='karyakartya',
            new_name='dakhla',
        ),
        migrations.RenameField(
            model_name='gayakvad',
            old_name='anujati',
            new_name='from1',
        ),
        migrations.RenameField(
            model_name='gayakvad',
            old_name='business',
            new_name='from2',
        ),
        migrations.RenameField(
            model_name='gayakvad',
            old_name='patni_hyat',
            new_name='from3',
        ),
        migrations.RenameField(
            model_name='gayakvad',
            old_name='vyakti_sahitya',
            new_name='lekha_pari',
        ),
        migrations.RenameField(
            model_name='gayakvad',
            old_name='education',
            new_name='sambandhit',
        ),
        migrations.RenameField(
            model_name='gayakvad',
            old_name='purava',
            new_name='vaishishtya1',
        ),
        migrations.RemoveField(
            model_name='gayakvad',
            name='age',
        ),
        migrations.RemoveField(
            model_name='gayakvad',
            name='itar',
        ),
        migrations.RemoveField(
            model_name='gayakvad',
            name='jya_sanstha',
        ),
        migrations.RemoveField(
            model_name='gayakvad',
            name='karkarta_sadhya',
        ),
        migrations.RemoveField(
            model_name='gayakvad',
            name='samajik',
        ),
        migrations.RemoveField(
            model_name='gayakvad',
            name='samkaly_kshetra',
        ),
        migrations.RemoveField(
            model_name='gayakvad',
            name='shifaras',
        ),
        migrations.RemoveField(
            model_name='gayakvad',
            name='thikan',
        ),
        migrations.RemoveField(
            model_name='gayakvad',
            name='vidhanmandal',
        ),
        migrations.RemoveField(
            model_name='gayakvad',
            name='vyakti_karyakarta',
        ),
        migrations.RemoveField(
            model_name='gayakvad',
            name='vyakti_karyakarta1',
        ),
        migrations.RemoveField(
            model_name='gayakvad',
            name='yapurvi_bahu',
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='mob1',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='mob2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='name2',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='padadhi1_name',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='padadhi2_name',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='pari_date1',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='pari_date2',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='pari_date3',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='pari_name1',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='pari_name2',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='pari_name3',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='sadar_sansthes',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='sambandhit_sanstha',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='swatantra_lekha',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='upkram',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='upvidhi',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='vaishishtya',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='varshik_aha',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='gayakvad',
            name='vyaktigat',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='gayakvad',
            name='arj_pur',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]