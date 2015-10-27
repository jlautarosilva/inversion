# -*- coding: utf-8 -*-
from django.contrib.gis import admin
from models import Inversion
from models import Bip
#Para incorporar botones import-export en admin web
from import_export.admin import ImportExportModelAdmin
#Para incorporar import-export en la aplicación
from import_export import resources

class BipResource(resources.ModelResource):

# Agregar acá before_import o get_or_init_instance segun corresponda
# Revisar https://github.com/django-import-export/django-import-export/issues/319
    #def before_import(self, dataset, dry_run, **kwargs):
        

    class Meta:
        model = Bip
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ['codigo_bip']
    

class BipAdmin(ImportExportModelAdmin):
    resource_class = BipResource
    pass


admin.site.register(Inversion, admin.GeoModelAdmin)
admin.site.register(Bip, BipAdmin)
