from django.contrib.gis.db import models as gis_models
from django.db import models
from django.contrib.auth import models as auth_models
from model_utils.managers import InheritanceManagerMixin

class GeoInheritanceManager(InheritanceManagerMixin, gis_models.GeoManager):
    pass

class Entity(gis_models.Model):
    position = gis_models.PointField()
    objects = GeoInheritanceManager()

class User(auth_models.AbstractUser, Entity):
    pass