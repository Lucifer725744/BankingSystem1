# Generated by Django 3.1.7 on 2021-04-14 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customers',
            new_name='Customer',
        ),
        migrations.RenameModel(
            old_name='Transfers',
            new_name='Transfer',
        ),
    ]
