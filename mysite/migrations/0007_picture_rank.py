# Generated by Django 3.0 on 2022-02-13 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20220211_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='rank',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]