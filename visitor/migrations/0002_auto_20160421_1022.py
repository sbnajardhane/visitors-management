# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-21 10:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email_id',
            field=models.CharField(blank=True, default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='person',
            name='mobile_no',
            field=models.CharField(blank=True, default='None', max_length=255),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 21, 10, 22, 45, 331007), max_length=255),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 21, 10, 22, 45, 329969), max_length=255),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='intime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, max_length=255),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='outtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, max_length=255),
        ),
    ]
