# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastDBUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastupdate', models.DateTimeField()),
            ],
        ),
    ]