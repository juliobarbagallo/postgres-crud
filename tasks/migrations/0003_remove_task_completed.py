# Generated by Django 4.0.6 on 2022-07-20 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
    ]
