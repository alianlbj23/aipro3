# Generated by Django 3.0 on 2022-02-13 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_picture_rank'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='picture',
            options={'ordering': ['-rank']},
        ),
    ]