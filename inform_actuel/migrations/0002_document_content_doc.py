# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-16 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inform_actuel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='content_doc',
            field=models.TextField(null=True),
        ),
    ]
