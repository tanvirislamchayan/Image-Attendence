# Generated by Django 5.0.7 on 2024-07-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_departmets_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmets',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='departmets',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='departmets',
            name='short_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
