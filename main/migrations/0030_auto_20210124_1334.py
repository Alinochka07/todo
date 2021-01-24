# Generated by Django 3.1.5 on 2021-01-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20210124_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('genre', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=100)),
                ('year', models.DateField(null=True)),
                ('books_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField(null=True)),
                ('is_favorites', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
