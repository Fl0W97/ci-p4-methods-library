# Generated by Django 4.2.7 on 2024-11-09 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_methods', '0008_method_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='method',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
