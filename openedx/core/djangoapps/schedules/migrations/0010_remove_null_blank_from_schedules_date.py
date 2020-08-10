# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-18 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0009_schedule_copy_column_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='start_date',
            field=models.DateTimeField(db_index=True, help_text='Date this schedule went into effect'),
        ),
    ]