# Generated by Django 3.1.6 on 2021-02-11 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swvl_admin', '0002_auto_20210209_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='captin',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='swvl_admin.captin'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='from_address',
            field=models.TextField(default='', null=True),
        ),
    ]
