# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('new', 'New'), ('processed', 'Processed'), ('printed', 'Printed')], default='new', max_length=16)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('data', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
