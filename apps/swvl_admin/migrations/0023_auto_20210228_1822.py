# Generated by Django 3.1.7 on 2021-02-28 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swvl_admin', '0022_auto_20210228_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 18, 22, 32, 813087)),
        ),
    ]
