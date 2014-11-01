from django.contrib.gis.db import models as gis_models
from django.db import models
from django.contrib.auth import models as auth_models

class Entity(gis_models.Model):
    position = gis_models.PointField()
    objects = gis_models.GeoManager()

class User(auth_models.AbstractUser, Entity):
    pass