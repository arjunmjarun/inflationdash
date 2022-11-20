# Generated by Django 4.1.3 on 2022-11-20 18:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyCPI',
            fields=[
                ('monthly_cpi_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cpi_date', models.DateField()),
                ('cpi_year', models.IntegerField()),
                ('cpi_month', models.IntegerField()),
                ('cpi_year_month', models.TextField()),
                ('cpi_description', models.TextField()),
                ('cpi', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
