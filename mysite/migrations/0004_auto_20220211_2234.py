# Generated by Django 3.0 on 2022-02-11 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20220209_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.URLField(),
        ),
    ]
