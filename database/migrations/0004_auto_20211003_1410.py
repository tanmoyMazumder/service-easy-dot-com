# Generated by Django 3.2.7 on 2021-10-03 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20211002_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='central_authority',
            old_name='ca_id',
            new_name='authority_id',
        ),
        migrations.RenameField(
            model_name='central_authority',
            old_name='ca_name',
            new_name='authority_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='cus_id',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='cus_name',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='manager',
            old_name='m_id',
            new_name='manager_id',
        ),
        migrations.RenameField(
            model_name='manager',
            old_name='m_name',
            new_name='manager_name',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='cus_id',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='s_id',
            new_name='service_id',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='sp_id',
            new_name='service_provider_id',
        ),
        migrations.RenameField(
            model_name='service_provider',
            old_name='s_id',
            new_name='service_id',
        ),
        migrations.RenameField(
            model_name='service_provider',
            old_name='sp_id',
            new_name='service_provider_id',
        ),
        migrations.RenameField(
            model_name='service_provider',
            old_name='sp_name',
            new_name='service_provider_name',
        ),
        migrations.RenameField(
            model_name='service_type',
            old_name='s_id',
            new_name='service_id',
        ),
        migrations.RenameField(
            model_name='service_type',
            old_name='s_name',
            new_name='service_name',
        ),
    ]
