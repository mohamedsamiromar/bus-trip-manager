# Generated by Django 3.1.7 on 2021-03-11 02:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swvl_admin', '0031_auto_20210307_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 11, 4, 38, 55, 463812)),
        ),
    ]
