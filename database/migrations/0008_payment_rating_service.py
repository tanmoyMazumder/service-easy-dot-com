# Generated by Django 3.2.7 on 2021-10-05 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_admin_table_customer_service_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_number', models.CharField(max_length=10)),
                ('problem', models.TextField()),
                ('address', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consumer', to='database.customer')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s_service', to='database.service_type')),
                ('service_provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider', to='database.admin_table')),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('review', models.CharField(max_length=300)),
                ('receipt_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billNumber', to='database.service')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_bill', models.IntegerField()),
                ('payment_method', models.CharField(max_length=25)),
                ('provider_paid', models.DateField()),
                ('authority_paid', models.DateField()),
                ('receipt_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipt', to='database.service')),
            ],
            options={
                'verbose_name_plural': 'Payment',
            },
        ),
    ]
