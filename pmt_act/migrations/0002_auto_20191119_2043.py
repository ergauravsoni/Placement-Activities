# Generated by Django 2.2.7 on 2019-11-19 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pmt_act', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enroll_tw',
            name='enrolled',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='enroll_tw',
            name='tw_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pmt_act.Trainings_Workshops'),
        ),
        migrations.AlterField(
            model_name='enroll_tw',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trainings_workshops',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
