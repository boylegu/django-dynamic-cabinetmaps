from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

                       url(r'^cabinetmaps/', include('demo.urls'))
                       )
