from django.contrib.gis.db import models as gis_models
from django.db import models
from django.contrib.auth import models as auth_models

class Entity():
    position = gis_models.PointField()
    objects = gis_models.GeoManager()

class User(auth_models.User, Entity):
    pass