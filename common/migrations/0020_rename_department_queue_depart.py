# Generated by Django 3.2.6 on 2021-09-15 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0019_queue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='queue',
            old_name='department',
            new_name='depart',
        ),
    ]
