# Generated by Django 5.0.7 on 2024-07-18 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjects',
            old_name='departmet',
            new_name='department',
        ),
    ]