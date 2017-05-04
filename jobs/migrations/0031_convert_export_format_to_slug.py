# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-28 23:01
from __future__ import unicode_literals

from django.contrib.postgres.fields import ArrayField
from django.db import migrations
from django.db.models.fields import CharField


class Migration(migrations.Migration):
    def convert_export_format_to_slug(apps, schema_editor):
        Job = apps.get_model('jobs', 'Job')
        for job in Job.objects.all():
            job.export_formats = map(lambda f: f.slug, job.formats.all())
            job.save()


    dependencies = [
        ('jobs', '0030_add_gpkg_export_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='export_formats',
            field=ArrayField(base_field=CharField(max_length=10), default=list, size=None),
        ),
        migrations.RunPython(convert_export_format_to_slug),
        migrations.RemoveField(
            model_name='job',
            name='formats',
        ),
        migrations.DeleteModel(
            name='ExportFormat',
        ),
    ]
