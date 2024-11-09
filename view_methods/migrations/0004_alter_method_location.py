# Generated by Django 4.2.16 on 2024-11-03 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_methods', '0003_alter_method_alt_atr_alter_method_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='method',
            name='location',
            field=models.CharField(choices=[('indoor', 'Indoor'), ('outdoor', 'Outdoor'), ('indoor/outdoor', 'Indoor/Outdoor')], default='indoor'),
        ),
    ]