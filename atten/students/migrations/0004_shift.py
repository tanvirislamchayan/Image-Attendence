# Generated by Django 5.0.7 on 2024-07-18 19:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_delete_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
