# Generated by Django 5.0.7 on 2024-07-24 20:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_initial'),
        ('teachers', '0003_alter_teacherprofile_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gendate',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='gendate',
            name='start_date',
        ),
        migrations.AddField(
            model_name='gendate',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gendate',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacherprofile'),
        ),
    ]