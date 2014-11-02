from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.api import UserResource

user_resource = UserResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ServerSuperheroes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(user_resource.urls)),
)
