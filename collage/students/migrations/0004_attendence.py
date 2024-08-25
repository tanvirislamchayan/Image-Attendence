# Generated by Django 5.0.7 on 2024-07-27 18:15

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collages', '0003_collage_slug'),
        ('departments', '0002_departments_field_departments_slug'),
        ('students', '0003_remove_gendate_end_date_remove_gendate_start_date_and_more'),
        ('subjects', '0001_initial'),
        ('teachers', '0003_alter_teacherprofile_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('collage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendence_collage', to='collages.collage')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendence_department', to='departments.departments')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attendence_group', to='students.studentshift')),
                ('probidhan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attendence_probidhan', to='subjects.probidhan')),
                ('semester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attendence_semester', to='subjects.semester')),
                ('students', models.ManyToManyField(to='students.student')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attendence_subject', to='subjects.subjects')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attendence_teacher', to='teachers.teacherprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
