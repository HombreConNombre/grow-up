# Generated by Django 5.2 on 2025-04-12 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegularUser',
            new_name='Users',
        ),
    ]
