# Generated by Django 3.2.7 on 2021-10-05 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_payment_rating_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_table',
            name='nid',
            field=models.CharField(max_length=17),
        ),
    ]
