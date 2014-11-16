from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api

from core.api import UserResource


v1_api = Api(api_name='v1')
v1_api.register(UserResource())

urlpatterns = patterns('',
   # Examples:
   # url(r'^$', 'ServerSuperheroes.views.home', name='home'),
   # url(r'^blog/', include('blog.urls')),

   #url(r'^api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),

   url(r'^api/doc/',
       include('tastypie_swagger.urls', namespace='tastypie_swagger'),
       kwargs={
           'tastypie_api_module': 'ServerSuperheroes.urls.v1_api',
           'namespace': 'core_tastypie_swagger',
           'version': '1'
       }
   ),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^api/', include(v1_api.urls)),
)
