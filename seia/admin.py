from django.contrib.gis import admin

from models import CalifiTotal15Utm

admin.site.register(CalifiTotal15Utm, admin.GeoModelAdmin)
