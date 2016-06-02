from django.conf.urls import patterns, include, url
from django.contrib import admin
import nn_web.views as v

urlpatterns = patterns('nn_web.views',

    url(r'^test/', 'test'),
)
