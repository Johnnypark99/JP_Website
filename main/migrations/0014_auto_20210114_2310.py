# Generated by Django 3.1.5 on 2021-01-14 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210105_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='file',
            name='title',
        ),
    ]
