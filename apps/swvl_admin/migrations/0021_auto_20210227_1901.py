# Generated by Django 3.1.7 on 2021-02-27 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swvl_admin', '0020_auto_20210227_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 27, 19, 1, 2, 650683)),
        ),
    ]
