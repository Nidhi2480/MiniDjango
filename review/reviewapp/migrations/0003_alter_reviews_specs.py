# Generated by Django 4.2.7 on 2023-11-15 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewapp', '0002_rename_review_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='specs',
            field=models.CharField(max_length=1500),
        ),
    ]
