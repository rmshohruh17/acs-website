# Generated by Django 4.1.5 on 2023-01-17 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_post_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='time',
        ),
        migrations.AddField(
            model_name='item',
            name='time',
            field=models.CharField(default='1h 30m', max_length=100),
        ),
    ]
