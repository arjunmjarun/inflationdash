# Generated by Django 4.1.3 on 2022-11-20 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inflation', '0002_monthlycpi_cpi_internal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlycpi',
            name='cpi',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
    ]