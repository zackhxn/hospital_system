# Generated by Django 3.2.6 on 2021-09-11 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20)),
                ('old', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=200)),
                ('phonenumber', models.CharField(max_length=200)),
                ('outpatient_id', models.CharField(max_length=200)),
            ],
        ),
    ]
