from django.contrib.gis import admin
from models import Inversion

admin.site.register(Inversion, admin.GeoModelAdmin)
