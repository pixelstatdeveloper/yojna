# Generated by Django 3.2 on 2021-10-12 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0009_auto_20211012_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upajivikesathi',
            old_name='courses',
            new_name='dharma',
        ),
        migrations.RenameField(
            model_name='upajivikesathi',
            old_name='shaishnik_patrata',
            new_name='education',
        ),
        migrations.AddField(
            model_name='upajivikesathi',
            name='birth_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='upajivikesathi',
            name='course_prashikshan',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='upajivikesathi',
            name='fa_name',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='upajivikesathi',
            name='gender',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='upajivikesathi',
            name='jat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='upajivikesathi',
            name='kau_prashikshan',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='upajivikesathi',
            name='prashikshan',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='upajivikesathi',
            name='pravarg',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='upajivikesathi',
            name='rahivasi',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='upajivikesathi',
            name='second_name',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='upajivikesathi',
            name='shakha',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='upajivikesathi',
            name='signature',
            field=models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign'),
        ),
        migrations.AddField(
            model_name='upajivikesathi',
            name='vikas_prashikshan',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]