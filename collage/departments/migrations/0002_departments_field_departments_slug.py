# Generated by Django 5.0.7 on 2024-07-24 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='field',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='departments',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
