from django.contrib.gis import admin

from models import Arauco

admin.site.register(Arauco, admin.GeoModelAdmin)
