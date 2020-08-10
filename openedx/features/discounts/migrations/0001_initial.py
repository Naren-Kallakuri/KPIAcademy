# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 20:08


import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import openedx.core.djangoapps.config_model_utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course_overviews', '0014_courseoverview_certificate_available_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountRestrictionConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateTimeField(auto_now_add=True, verbose_name='Change date')),
                ('enabled', models.NullBooleanField(default=None, verbose_name='Enabled')),
                ('org', models.CharField(blank=True, db_index=True, help_text='Configure values for all course runs associated with this Organization. This is the organization string (i.e. edX, MITx).', max_length=255, null=True)),
                ('org_course', models.CharField(blank=True, db_index=True, help_text="Configure values for all course runs associated with this course. This is should be formatted as 'org+course' (i.e. MITx+6.002x, HarvardX+CS50).", max_length=255, null=True, validators=[openedx.core.djangoapps.config_model_utils.models.validate_course_in_org], verbose_name='Course in Org')),
                ('disabled', models.NullBooleanField(default=None, verbose_name='Disabled')),
                ('changed_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Changed by')),
                ('course', models.ForeignKey(blank=True, help_text='Configure values for this course run. This should be formatted as the CourseKey (i.e. course-v1://MITx+6.002x+2019_Q1)', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course_overviews.CourseOverview', verbose_name='Course Run')),
                ('site', models.ForeignKey(blank=True, help_text='Configure values for all course runs associated with this site.', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='discountrestrictionconfig',
            index=models.Index(fields=['site', 'org', 'course'], name='discounts_d_site_id_d67da3_idx'),
        ),
        migrations.AddIndex(
            model_name='discountrestrictionconfig',
            index=models.Index(fields=['site', 'org', 'org_course', 'course'], name='discounts_d_site_id_f83727_idx'),
        ),
    ]
