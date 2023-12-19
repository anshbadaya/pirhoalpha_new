# Generated by Django 4.1.13 on 2023-12-07 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='building',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='floor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='state',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
