from django.contrib.gis.db import models

class Arauco(models.Model):
    id = models.FloatField(primary_key=True)
    fech_plani = models.DateField()
    respon_eje = models.CharField(max_length=254)
    codigo_bip = models.FloatField()
    x = models.FloatField()
    y = models.FloatField()
    nombre = models.CharField(max_length=254)
    iniciativa = models.CharField(max_length=254)
    comuna = models.CharField(max_length=254)
    etapa_post = models.CharField(max_length=254)
    sector = models.CharField(max_length=254)
    area = models.CharField(max_length=254)
    cos_totm_field = models.FloatField()
    financiera = models.CharField(max_length=254)
    glosa_conv = models.CharField(max_length=254)
    rezago_mop = models.CharField(max_length=254)
    rate = models.CharField(max_length=254)
    fecha_rate = models.CharField(max_length=254)
    n_cer_core = models.CharField(max_length=254)
    fecha_cer = models.CharField(max_length=254, null=True, blank=True)
    situacion = models.CharField(max_length=254)
    tipologia = models.CharField(max_length=254)
    meca_finan = models.CharField(max_length=254)
    cartera = models.CharField(max_length=254)
    exitos = models.CharField(max_length=254)
    temporalid = models.CharField(max_length=254)
    _2014 = models.CharField(max_length=254)
    _2015 = models.FloatField()
    _2016 = models.FloatField()
    _2017 = models.CharField(max_length=254)
    _2018 = models.CharField(max_length=254)
    _2019 = models.CharField(max_length=254)
    _2020 = models.CharField(max_length=254)
    _2021 = models.CharField(max_length=254)
    _2022 = models.CharField(max_length=254)
    _2023 = models.CharField(max_length=254)
    n_corr_ugi = models.FloatField()
    ano_presen = models.FloatField()
    ano_presup = models.FloatField()
    cod_bip = models.FloatField()
    nombre_del = models.CharField(max_length=254)
    comuna_1 = models.CharField(max_length=254)
    provincia = models.CharField(max_length=254)
    certif_co = models.FloatField()
    fecha_cert = models.DateField(null=True, blank=True)
    tipologias = models.CharField(max_length=254)
    unidad_tec = models.CharField(max_length=254)
    subtit_ulo = models.FloatField()
    items = models.FloatField()
    asignacion = models.FloatField()
    resolucion = models.CharField(max_length=254)
    fech_cmand = models.DateField(null=True, blank=True)
    monto_cman = models.FloatField()

    geom = models.MultiPointField(srid=32718)
    objects = models.GeoManager()

    def __str__(self):
        return str(self.id)
