# Generated by Django 3.1.6 on 2021-02-27 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swvl_admin', '0017_auto_20210226_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='total_price',
            field=models.IntegerField(null=True),
        ),
    ]