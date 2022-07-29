# Generated by Django 3.2.8 on 2021-11-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0033_auto_20211105_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='review',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='time',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]