from django.conf.urls import patterns, include, url
from django.contrib import admin
import nn_web.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nn_boost.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^nn/', include(nn_web.urls))
)
