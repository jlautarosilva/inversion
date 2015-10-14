from django.contrib.gis import admin
from models import Inversion
from import_export.admin import ImportExportModelAdmin
#solo para ejemplo
from django.core.models import Book


admin.site.register(Inversion, admin.GeoModelAdmin)

class BookResource(resources.ModelResource):
    class Meta:
        model = Book

class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource
    pass
