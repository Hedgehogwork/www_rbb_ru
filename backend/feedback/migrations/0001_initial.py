# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import feedback.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('body', models.TextField(verbose_name='message')),
                ('file1', models.FileField(upload_to=feedback.models.update_filename)),
                ('file2', models.FileField(upload_to=feedback.models.update_filename)),
                ('file3', models.FileField(upload_to=feedback.models.update_filename)),
                ('sent_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'feedback',
                'verbose_name_plural': 'feedbacks',
            },
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('receivers', models.ManyToManyField(to='feedback.Receiver')),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='theme',
            field=models.ForeignKey(to='feedback.Theme'),
        ),
    ]
