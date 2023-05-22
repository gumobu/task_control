# Generated by Django 4.2.1 on 2023-05-15 20:25

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_date', models.DateTimeField(default=datetime.datetime(2023, 5, 15, 20, 25, 23, 200214, tzinfo=datetime.timezone.utc))),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
