# Generated by Django 3.1.5 on 2021-01-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20210123_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='cost_amount',
            field=models.IntegerField(null=True),
        ),
    ]