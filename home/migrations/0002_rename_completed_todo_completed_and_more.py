# Generated by Django 4.1.4 on 2022-12-07 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='Completed',
            new_name='completed',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='Pending',
            new_name='pending',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='Task',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='Time',
            new_name='time',
        ),
    ]