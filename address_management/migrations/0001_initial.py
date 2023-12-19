# Generated by Django 4.1.13 on 2023-12-07 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'area_management',
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address_management.area')),
            ],
            options={
                'db_table': 'building_management',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'country_management',
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address_management.building')),
            ],
            options={
                'db_table': 'floor_management',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address_management.country')),
            ],
            options={
                'db_table': 'state_management',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address_management.floor')),
            ],
            options={
                'db_table': 'room_management',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address_management.state')),
            ],
            options={
                'db_table': 'city_management',
            },
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address_management.city'),
        ),
    ]
