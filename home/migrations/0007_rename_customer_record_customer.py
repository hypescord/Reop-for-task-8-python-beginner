# Generated by Django 4.0.5 on 2022-06-19 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_record_end_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='Customer',
            new_name='customer',
        ),
    ]