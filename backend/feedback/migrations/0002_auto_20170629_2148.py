# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import feedback.models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='ip',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='file1',
            field=models.FileField(null=True, upload_to=feedback.models.update_filename, blank=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='file2',
            field=models.FileField(null=True, upload_to=feedback.models.update_filename, blank=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='file3',
            field=models.FileField(null=True, upload_to=feedback.models.update_filename, blank=True),
        ),
    ]
