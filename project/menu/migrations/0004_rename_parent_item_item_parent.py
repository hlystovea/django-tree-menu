# Generated by Django 4.1.5 on 2023-01-04 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_remove_item_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='parent_item',
            new_name='parent',
        ),
    ]