# Generated by Django 3.1.5 on 2021-01-22 11:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20210122_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='year',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]