# Generated by Django 4.1.5 on 2023-01-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_remove_post_time_item_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
