# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 13:45
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
                ('status',
                 models.CharField(choices=[('new', 'New'), ('processed', 'Processed'), ('printed', 'Printed')],
                                  default='new', max_length=16)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('data', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('key', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('path', models.FileField(upload_to=b'')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
