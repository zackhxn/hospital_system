# Generated by Django 3.2.6 on 2021-09-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_medicine'),
    ]

    operations = [
        migrations.CreateModel(
            name='manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='medicine',
            name='number',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.BigIntegerField(),
        ),
    ]
