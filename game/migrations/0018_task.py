# Generated by Django 4.2.2 on 2023-06-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0017_rename_units_archer_village_archer_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('task_id', models.CharField(max_length=36)),
                ('has_ended', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
