# Generated by Django 4.2.5 on 2023-09-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_lesson_viewed_status_lesson_viewed_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='duration_seconds',
            field=models.PositiveIntegerField(),
        ),
    ]