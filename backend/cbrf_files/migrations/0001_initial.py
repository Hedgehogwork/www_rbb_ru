# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CBRF_Deposit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('photo', models.FileField(upload_to=b'cbrf_deposit')),
            ],
        ),
    ]
