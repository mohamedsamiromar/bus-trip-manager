# Generated by Django 3.1.7 on 2021-03-04 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swvl_admin', '0026_auto_20210304_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date_For_start_trip',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 4, 17, 10, 39, 275776)),
        ),
    ]
