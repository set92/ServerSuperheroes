from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from core.models import User


class UserResource(ModelResource):
    class Meta:
        resource_name = 'user'
        queryset = User.objects.all()
        authorization = Authorization()