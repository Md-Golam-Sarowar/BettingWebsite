# Generated by Django 3.1.6 on 2021-03-21 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BettingApp', '0011_auto_20210321_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybet',
            name='user',
            field=models.ForeignKey(default=36, on_delete=django.db.models.deletion.CASCADE, to='BettingApp.userinfo'),
            preserve_default=False,
        ),
    ]