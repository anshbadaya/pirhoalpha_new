# Generated by Django 4.1.13 on 2023-12-07 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0003_rename_id_category_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_id',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='soldbillingdetails',
            name='products',
        ),
    ]
