# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-10 19:09
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    def filename_to_filenames(apps, schema_editor):
        ExportTask = apps.get_model('tasks', 'ExportTask')
        for task in ExportTask.objects.all():
            task.filenames = [task.filename]
            task.save()

    dependencies = [
        ('tasks', '0031_exporttask_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='exporttask',
            name='filenames',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50, null=True), default=list, size=None),
        ),
        migrations.RunPython(filename_to_filenames)
    ]
