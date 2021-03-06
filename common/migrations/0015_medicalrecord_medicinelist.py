# Generated by Django 3.2.6 on 2021-09-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_medicinemanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicalrecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.BigIntegerField()),
                ('doctor_id', models.BigIntegerField()),
                ('department', models.CharField(max_length=200)),
                ('medicinelist_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='medicinelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicalrecord_id', models.BigIntegerField()),
                ('patient_id', models.BigIntegerField()),
                ('name', models.CharField(max_length=200)),
                ('price', models.BigIntegerField()),
                ('number', models.BigIntegerField()),
            ],
        ),
    ]
