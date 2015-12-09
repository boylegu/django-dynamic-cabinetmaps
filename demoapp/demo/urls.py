from django.conf.urls import patterns, url

from demo.views import CMDB

urlpatterns = patterns('',

                       url(r'^$', CMDB.as_view())
                       )
