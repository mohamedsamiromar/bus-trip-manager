# Generated by Django 3.1.7 on 2021-03-11 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swvlauthentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
