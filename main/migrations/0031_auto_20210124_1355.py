# Generated by Django 3.1.5 on 2021-01-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20210124_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookshop',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
