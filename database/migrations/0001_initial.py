# Generated by Django 3.2.7 on 2021-10-01 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_id', models.CharField(max_length=8)),
                ('area_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Central_Authority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ca_id', models.CharField(max_length=8)),
                ('ca_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_id', models.CharField(max_length=8)),
                ('cus_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=8)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_area', to='database.area')),
            ],
        ),
        migrations.CreateModel(
            name='Service_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.CharField(max_length=8)),
                ('s_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_id', models.CharField(max_length=8)),
                ('sp_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=11)),
                ('nid', models.CharField(max_length=17)),
                ('password', models.CharField(max_length=8)),
                ('s_id', models.CharField(max_length=100)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider_area', to='database.area')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_number', models.IntegerField()),
                ('problem', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=70)),
                ('date', models.CharField(max_length=12)),
                ('time', models.CharField(max_length=12)),
                ('cus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consumer', to='database.customer')),
                ('s_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s_service', to='database.service_type')),
                ('sp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider', to='database.service_provider')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('review', models.CharField(max_length=300)),
                ('receipt_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='took_service', to='database.service')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_bill', models.IntegerField()),
                ('payment_method', models.CharField(max_length=25)),
                ('provider_paid', models.CharField(max_length=12)),
                ('authority_paid', models.CharField(max_length=12)),
                ('receipt_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipt', to='database.service')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.CharField(max_length=8)),
                ('m_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=11)),
                ('nid', models.CharField(max_length=17)),
                ('password', models.CharField(max_length=8)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager_area', to='database.area')),
            ],
        ),
    ]
