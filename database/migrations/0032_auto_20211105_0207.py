# Generated by Django 3.0.8 on 2021-11-04 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0031_auto_20211105_0152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service_type',
            old_name='service_category',
            new_name='category',
        ),
    ]