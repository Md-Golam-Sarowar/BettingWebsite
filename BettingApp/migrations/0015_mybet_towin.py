# Generated by Django 3.1.6 on 2021-03-25 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BettingApp', '0014_auto_20210325_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybet',
            name='toWin',
            field=models.FloatField(default=0),
        ),
    ]
