# Generated by Django 3.1.5 on 2021-01-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210122_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
