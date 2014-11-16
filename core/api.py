from functools import partial

from django.conf.urls import url

from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.utils.urls import trailing_slash

from core.bussiness import get_near_objects

from core.models import User
from utils import custom_resource


class UserResource(ModelResource):

    def __init__(self, *args, **kwargs):
        self.list_near_objects_par = partial(custom_resource, self, get_near_objects)
        super(UserResource, self).__init__(*args, **kwargs)

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>\w+)/objects%s$" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('list_near_objects_par')),
        ]

    class Meta:
        resource_name = 'user'
        queryset = User.objects.all()
        authorization = Authorization()

