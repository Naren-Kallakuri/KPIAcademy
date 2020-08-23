"""
URLs for KPIViews app
"""

from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.views import password_reset_complete

from . import views


urlpatterns = [

    url(r'^aboutus/?$', views.getAboutUs, name='About Us'),
    url(r'^app/(?P<os>[^/]*)?$', views.getMobileApp, name='App'),

]