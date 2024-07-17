# Generated by Django 5.0.7 on 2024-07-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_remove_teacherprofile_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherprofile',
            name='qualification',
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='hiest_digree',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='versity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
