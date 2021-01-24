# Generated by Django 3.1.5 on 2021-01-22 13:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210122_1137'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.AddField(
            model_name='books',
            name='cost_amount',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
