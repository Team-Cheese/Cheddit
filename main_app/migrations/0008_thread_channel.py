# Generated by Django 4.0.3 on 2022-04-11 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_merge_20220411_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.channel'),
        ),
    ]
