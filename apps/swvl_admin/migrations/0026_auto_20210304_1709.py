# Generated by Django 3.1.7 on 2021-03-04 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swvl_admin', '0025_auto_20210304_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date_For_start_trip',
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 4, 17, 9, 44, 425282)),
        ),
    ]
