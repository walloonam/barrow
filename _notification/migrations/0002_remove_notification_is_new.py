# Generated by Django 4.1.3 on 2023-01-12 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_notification', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='is_new',
        ),
    ]