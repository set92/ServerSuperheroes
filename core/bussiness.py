from __future__ import print_function, unicode_literals
from django.contrib.gis.measure import D
from core.models import User, Entity

__author__ = 'javier'

def get_near_objects(**kwargs):
    user_id = kwargs['pk']
    user = User.objects.get(id=user_id)
    objects = Entity.objects.filter(position__distance_lte=(user.position, D(km=1)))
    return objects
