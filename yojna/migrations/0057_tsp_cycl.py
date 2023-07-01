# Generated by Django 3.2 on 2021-11-29 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0056_scp_cycl'),
    ]

    operations = [
        migrations.CreateModel(
            name='tsp_cycl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('sam_patta', models.CharField(blank=True, max_length=1000, null=True)),
                ('mukkam', models.CharField(blank=True, max_length=1000, null=True)),
                ('post', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('taluka', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('jati', models.BooleanField(blank=True, default=None, null=True)),
                ('dakhla', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('jat', models.CharField(blank=True, max_length=100, null=True)),
                ('potjat', models.CharField(blank=True, max_length=100, null=True)),
                ('san', models.CharField(blank=True, max_length=100, null=True)),
                ('iyatta', models.CharField(blank=True, max_length=100, null=True)),
                ('sch_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('sch_patta', models.CharField(blank=True, max_length=1000, null=True)),
                ('gun', models.CharField(blank=True, max_length=100, null=True)),
                ('mulinmadhun', models.CharField(blank=True, max_length=100, null=True)),
                ('takke', models.CharField(blank=True, max_length=100, null=True)),
                ('san1', models.CharField(blank=True, max_length=100, null=True)),
                ('iyatta1', models.CharField(blank=True, max_length=100, null=True)),
                ('sch_name1', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('sch_patta1', models.CharField(blank=True, max_length=1000, null=True)),
                ('gav_name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('antar', models.CharField(blank=True, max_length=100, null=True)),
                ('buisness', models.CharField(blank=True, max_length=1000, null=True)),
                ('dakhla1', models.FileField(blank=True, default=None, null=True, upload_to='media/divyang_person_sign')),
                ('san2', models.CharField(blank=True, max_length=100, null=True)),
                ('utpanna', models.CharField(blank=True, max_length=100, null=True)),
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
                'db_table': 'tsp_cycl',
            },
        ),
    ]
