# Generated by Django 3.0.8 on 2021-10-30 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0026_auto_20211030_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='service_id',
        ),
        migrations.AddField(
            model_name='service',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Area'),
        ),
        migrations.AddField(
            model_name='service',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s_service', to='database.Service_type'),
        ),
    ]