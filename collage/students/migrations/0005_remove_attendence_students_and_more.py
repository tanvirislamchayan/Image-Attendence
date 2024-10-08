# Generated by Django 5.0.7 on 2024-07-27 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_attendence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendence',
            name='students',
        ),
        migrations.AddField(
            model_name='attendence',
            name='absent_students',
            field=models.ManyToManyField(blank=True, related_name='absent_attendences', to='students.student'),
        ),
        migrations.AddField(
            model_name='attendence',
            name='present_students',
            field=models.ManyToManyField(blank=True, related_name='present_attendences', to='students.student'),
        ),
    ]
