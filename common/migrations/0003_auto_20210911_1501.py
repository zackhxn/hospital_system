# Generated by Django 3.2.6 on 2021-09-11 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='old',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
