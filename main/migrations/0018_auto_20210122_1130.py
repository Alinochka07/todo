# Generated by Django 3.1.5 on 2021-01-22 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210122_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='price_amount',
            new_name='cost_amount',
        ),
    ]
