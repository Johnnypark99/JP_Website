# Generated by Django 3.1.4 on 2021-01-05 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210105_2020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='pdf',
            new_name='file',
        ),
    ]
