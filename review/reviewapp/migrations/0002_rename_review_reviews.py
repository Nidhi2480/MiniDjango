# Generated by Django 4.2.7 on 2023-11-13 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='review',
            new_name='reviews',
        ),
    ]