# Generated by Django 3.1.6 on 2021-02-24 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swvl_admin', '0014_trip_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
