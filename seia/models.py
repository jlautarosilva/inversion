# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models

class CalifiTotal15Utm(models.Model):
    fid = models.AutoField(primary_key=True)
    the_geom = models.PointField(srid=32718, blank=True, null=True)
    validacion = models.CharField(db_column='VALIDACION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=254, blank=True, null=True)  # Field name made lowercase.
    desc_field = models.CharField(db_column='DESC_', max_length=254, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    tipo = models.CharField(db_column='Tipo', max_length=254, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=254, blank=True, null=True)  # Field name made lowercase.
    tipologaa = models.CharField(db_column='TipologAa', max_length=254, blank=True, null=True)  # Field name made lowercase.
    titular = models.CharField(db_column='Titular', max_length=254, blank=True, null=True)  # Field name made lowercase.
    inversiomm = models.FloatField(db_column='InversioMM', blank=True, null=True)  # Field name made lowercase.
    fecha_pres = models.DateTimeField(db_column='Fecha_pres', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=254, blank=True, null=True)  # Field name made lowercase.
    fecha_cali = models.CharField(db_column='Fecha_cali', max_length=254, blank=True, null=True)  # Field name made lowercase.
    sector_pro = models.CharField(db_column='Sector_pro', max_length=254, blank=True, null=True)  # Field name made lowercase.
    log = models.FloatField(db_column='LOG', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='LAT', blank=True, null=True)  # Field name made lowercase.
    x = models.FloatField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    y = models.FloatField(db_column='Y', blank=True, null=True)  # Field name made lowercase.
    datum = models.FloatField(db_column='DATUM', blank=True, null=True)  # Field name made lowercase.
    huso = models.FloatField(db_column='HUSO', blank=True, null=True)  # Field name made lowercase.
    hiperlink = models.CharField(db_column='HIPERLINK', max_length=254, blank=True, null=True)  # Field name made lowercase.
    ene = models.CharField(db_column='ENE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    feb = models.CharField(db_column='FEB', max_length=15, blank=True, null=True)  # Field name made lowercase.
    maz = models.CharField(db_column='MAZ', max_length=15, blank=True, null=True)  # Field name made lowercase.
    abr = models.CharField(db_column='ABR', max_length=15, blank=True, null=True)  # Field name made lowercase.
    may = models.CharField(db_column='MAY', max_length=15, blank=True, null=True)  # Field name made lowercase.
    jun = models.CharField(db_column='JUN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    jul = models.CharField(db_column='JUL', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ago = models.CharField(db_column='AGO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sep = models.CharField(db_column='SEP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    oct = models.CharField(db_column='OCT', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nov = models.CharField(db_column='NOV', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dic = models.CharField(db_column='DIC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    mes_evalu = models.CharField(db_column='MES_EVALU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mes = models.CharField(db_column='MES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    aao_aprob = models.BigIntegerField(db_column='AAO_APROB', blank=True, null=True)  # Field name made lowercase.
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'califi_total15utm'

