# Generated by Django 3.1.5 on 2021-01-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_price_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='currency',
        ),
        migrations.AddField(
            model_name='price',
            name='price_amount',
            field=models.DecimalField(decimal_places=2, default='5', max_digits=9),
        ),
    ]
