# Generated by Django 4.2.1 on 2023-06-09 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0017_rename_units_archer_village_archer_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='is_connected',
        ),
    ]
