# Generated by Django 2.2.7 on 2019-11-19 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainings_Workshops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('banner', models.ImageField(blank=True, null=True, upload_to='banners/')),
                ('registration_Begins', models.DateTimeField(null=True)),
                ('registration_Ends', models.DateTimeField(null=True)),
                ('event_Begins', models.DateTimeField(null=True)),
                ('event_Fee', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('event_URL', models.URLField(blank=True, null=True)),
                ('additional_Details', models.TextField(blank=True, null=True)),
                ('contact_Name', models.CharField(max_length=50, null=True)),
                ('contact_Email', models.EmailField(max_length=254, null=True)),
                ('contact_No', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('document', models.FileField(blank=True, null=True, upload_to='document/')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Training/Workshop',
                'verbose_name_plural': 'Trainings/Workshops',
            },
        ),
        migrations.CreateModel(
            name='Enroll_TW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tw_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pmt_act.Trainings_Workshops')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Enroll_TW',
                'unique_together': {('user_id', 'tw_id')},
            },
        ),
    ]
