# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160127_2002'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blob',
        ),
        migrations.AlterField(
            model_name='order',
            name='data',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='file',
            field=models.TextField(blank=True, null=True),
        ),
    ]
