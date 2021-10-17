# Generated by Django 3.2.6 on 2021-09-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_auto_20210913_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='mdicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.BigIntegerField()),
                ('number', models.BigIntegerField()),
                ('remark', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='remark',
        ),
    ]
