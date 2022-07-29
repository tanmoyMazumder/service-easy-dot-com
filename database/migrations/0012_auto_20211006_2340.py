# Generated by Django 3.2.7 on 2021-10-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_alter_admin_table_area_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='authority_paid',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='provider_paid',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='review',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='service',
            name='time',
            field=models.TimeField(blank=True),
        ),
    ]
