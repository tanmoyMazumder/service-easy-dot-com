# Generated by Django 3.2.7 on 2021-10-02 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='receipt_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billNumber', to='database.service'),
        ),
        migrations.AlterField(
            model_name='service',
            name='receipt_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='service_provider',
            name='s_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.service_type'),
        ),
    ]