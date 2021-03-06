# Generated by Django 3.1.6 on 2021-03-08 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BettingApp', '0007_userinfo_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='bethistory',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='BettingApp.userinfo'),
        ),
        migrations.AddField(
            model_name='livesport',
            name='sportCategory',
            field=models.CharField(default='Tennis', max_length=250),
            preserve_default=False,
        ),
    ]
