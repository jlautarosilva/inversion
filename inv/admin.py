# -*- coding: utf-8 -*-
from django.contrib.gis import admin
from models import Inversion
from models import Bip
#Para incorporar botones import-export en admin web
from import_export.admin import ImportExportModelAdmin
#Para incorporar import-export en la aplicación
from import_export import resources

class BipResource(resources.ModelResource):
#    coordenadas = fields.Field()
    class Meta:
        model = Bip
        import_id_fields = ['codigo_bip']
    
#    def dehydrate(self, Bip):


class BipAdmin(ImportExportModelAdmin):
    resource_class = BipResource
    pass


admin.site.register(Inversion, admin.GeoModelAdmin)
admin.site.register(Bip, BipAdmin)

