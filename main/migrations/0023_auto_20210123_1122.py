# Generated by Django 3.1.5 on 2021-01-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_books_is_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='cost_amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='books',
            name='date',
            field=models.DateField(),
        ),
    ]
