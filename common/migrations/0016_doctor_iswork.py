# Generated by Django 3.2.6 on 2021-09-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0015_medicalrecord_medicinelist'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='iswork',
            field=models.BigIntegerField(default=0),
        ),
    ]
