# Generated by Django 3.0.8 on 2021-10-30 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0028_auto_20211030_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
    ]