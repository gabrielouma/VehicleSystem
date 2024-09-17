# Generated by Django 5.0.6 on 2024-08-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0005_remove_orders_vehicle_id_orders_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='vehicle_image',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='vehicle_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='vehicle_type',
            field=models.CharField(default=2, max_length=15),
            preserve_default=False,
        ),
    ]
