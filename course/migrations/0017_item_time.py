# Generated by Django 4.1.5 on 2023-01-18 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='time',
            field=models.CharField(default='1h 35m', max_length=50),
        ),
    ]
