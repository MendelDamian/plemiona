# Generated by Django 4.2.2 on 2023-06-13 15:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0022_battle_attacker_strenght_battle_defender_strenght'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='battle',
            unique_together=set(),
        ),
    ]
