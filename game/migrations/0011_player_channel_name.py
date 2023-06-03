# Generated by Django 4.2.1 on 2023-06-03 15:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_add_village_x_village_y'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='channel_name',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
