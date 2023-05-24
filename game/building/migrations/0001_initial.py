# Generated by Django 4.2.1 on 2023-05-24 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('level', models.IntegerField(default=1)),
                ('wood_production', models.IntegerField(default=0, help_text='Per second')),
                ('clay_production', models.IntegerField(default=0, help_text='Per second')),
                ('iron_production', models.IntegerField(default=0, help_text='Per second')),
                ('wood_cost', models.IntegerField(default=0)),
                ('clay_cost', models.IntegerField(default=0)),
                ('iron_cost', models.IntegerField(default=0)),
                ('upgrade_time', models.IntegerField(default=0, help_text='In seconds')),
                ('upgrades_from', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='upgrades_to', to='building.building')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Barracks',
            fields=[
                ('building_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='building.building')),
            ],
            options={
                'abstract': False,
            },
            bases=('building.building',),
        ),
        migrations.CreateModel(
            name='ClayPit',
            fields=[
                ('building_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='building.building')),
            ],
            options={
                'abstract': False,
            },
            bases=('building.building',),
        ),
        migrations.CreateModel(
            name='Granary',
            fields=[
                ('building_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='building.building')),
            ],
            options={
                'abstract': False,
            },
            bases=('building.building',),
        ),
        migrations.CreateModel(
            name='IronMine',
            fields=[
                ('building_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='building.building')),
            ],
            options={
                'abstract': False,
            },
            bases=('building.building',),
        ),
        migrations.CreateModel(
            name='Sawmill',
            fields=[
                ('building_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='building.building')),
            ],
            options={
                'abstract': False,
            },
            bases=('building.building',),
        ),
        migrations.CreateModel(
            name='TownHall',
            fields=[
                ('building_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='building.building')),
            ],
            options={
                'abstract': False,
            },
            bases=('building.building',),
        ),
    ]
