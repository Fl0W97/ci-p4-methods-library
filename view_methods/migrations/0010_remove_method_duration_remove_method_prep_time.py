# Generated by Django 4.2.7 on 2024-11-10 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view_methods', '0009_alter_method_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='method',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='method',
            name='prep_time',
        ),
    ]