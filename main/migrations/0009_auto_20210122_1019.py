# Generated by Django 3.1.5 on 2021-01-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210122_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
