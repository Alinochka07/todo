# Generated by Django 3.1.5 on 2021-01-22 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210120_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='books',
            name='genre',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.FloatField(verbose_name=int),
        ),
        migrations.AlterField(
            model_name='books',
            name='subtitle',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='year',
            field=models.IntegerField(verbose_name=int),
        ),
    ]
