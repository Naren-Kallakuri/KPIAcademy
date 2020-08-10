# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-31 18:13


import json
import logging

from ccx_keys.locator import CCXLocator
from django.db import migrations
from django.http import Http404

from lms.djangoapps.courseware.courses import get_course_by_id

log = logging.getLogger(__name__)


def save_display_name(apps, schema_editor):
    '''
    Add override for `display_name` for CCX courses that don't have one yet.
    '''
    CcxFieldOverride = apps.get_model('ccx', 'CcxFieldOverride')
    CustomCourseForEdX = apps.get_model('ccx', 'CustomCourseForEdX')

    # Build list of CCX courses that don't have an override for `display_name` yet
    ccx_display_name_present_ids = list(CcxFieldOverride.objects.filter(
        field='display_name').values_list('ccx__id', flat=True))
    ccx_list = CustomCourseForEdX.objects.exclude(id__in=ccx_display_name_present_ids)

    # Create `display_name` overrides for these CCX courses
    for ccx in ccx_list:
        try:
            course = get_course_by_id(ccx.course_id, depth=None)
        except Http404:
            log.error(
                "Root course %s not found. Can't create display_name override for %s.",
                ccx.course_id,
                ccx.display_name
            )
            continue
        display_name = course.fields['display_name']
        display_name_json = display_name.to_json(ccx.display_name)
        serialized_display_name = json.dumps(display_name_json)

        CcxFieldOverride.objects.get_or_create(
            ccx=ccx,
            location=course.location,
            field='display_name',
            defaults={'value': serialized_display_name},
        )


class Migration(migrations.Migration):

    dependencies = [
        ('ccx', '0005_change_ccx_coach_to_staff'),
    ]

    operations = [
        migrations.RunPython(save_display_name, reverse_code=migrations.RunPython.noop)
    ]