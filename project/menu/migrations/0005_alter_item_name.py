# Generated by Django 4.1.5 on 2023-01-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_rename_parent_item_item_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
    ]
