# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0003_auto_20161120_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotGames',
            fields=[
                ('appid', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('appid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('searchCount', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date', 'name'],
            },
        ),
    ]
