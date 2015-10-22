# -*- coding: utf-8 -*-
from django.contrib.gis.db import models

#Implementar validadores para los integerfield
from django.core.validators import MinValueValidator, MaxValueValidator

class Inversion(models.Model):

    num_corr = models.AutoField(primary_key=True)
    ano_postul = models.IntegerField("Ano postulacion",null=True, blank=True) #4
    situacion = models.IntegerField("Situacion",null=True, blank=True) # 0 a 9
    id_bip_n = models.IntegerField("Codigo BIP numero",null=True, blank=True) #8
    id_bip_t = models.CharField('Codigo BIP texto',max_length=8,null=True, blank=True)
    x = models.DecimalField(max_digits = 6, decimal_places = 3,null=True, blank=True)
    y = models.DecimalField(max_digits = 7, decimal_places = 6,null=True, blank=True)
    obs1 = models.IntegerField("OBS 1",null=True, blank=True) # 2
    cod_comu = models.IntegerField("Codigo comuna",null=True, blank=True) #4
    cod_corr = models.IntegerField("Codigo Corr",null=True, blank=True) #5
    cod_estado = models.IntegerField("Codigo Estado",null=True, blank=True) #2
    estado_postu = models.CharField('Estado de la Postulacion', max_length=18,null=True, blank=True)
    cod_proy_ugit = models.IntegerField('Codigo Proyecto UGIT',null=True, blank=True) #18
    rep_conadi = models.CharField('Rep CONADI', max_length=9,null=True, blank=True)
    nom_proy = models.CharField('Nombre del Proyecto',max_length=999,null=True, blank=True)
    n_cert_core = models.CharField('Numero certificado CORE', max_length=4,null=True, blank=True) #abc
    n_ses_core = models.IntegerField('Numero sersion CORE',null=True, blank=True) #4
    fec_core = models.DateField(null=True, blank=True)
    mont_pesos = models.IntegerField('Monto pesos',null=True, blank=True) #12
    fuen_finan = models.CharField(max_length=30,null=True, blank=True)
    comuna = models.CharField(max_length=20,null=True, blank=True)
    provincia = models.CharField(max_length=10,null=True, blank=True)
    terr_planif = models.CharField(max_length=20,null=True, blank=True)
    glosa = models.CharField(max_length=999,null=True, blank=True)
    tipologias = models.CharField(max_length=20,null=True, blank=True)
    sector = models.CharField(max_length=20,null=True, blank=True)
    sec_terr_com = models.CharField(max_length=999,null=True, blank=True)
    rate = models.CharField(max_length=2,null=True, blank=True)
    fec_rate = models.DateField(null=True, blank=True)


    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

class Bip (models.Model):
#    codigo_bip = models.IntegerField("Código BIP", primary_key=True)
    codigo_bip = models.CharField("Código BIP", max_length=10,primary_key=True)
    competencia = models.CharField("Competencia",max_length=10,null=True, blank=True)
    comuna = models.CharField("Comuna",max_length=20,null=True,blank=True)
    coordenadas = models.CharField("Coordenadas", max_length=9999, null=True, blank=True)
#    coordenadas = models.GeometryField("Coordenadas", null=True, blank=True)
    fecha_inicio_etapa_menor = models.CharField("Fecha de inicio Etapa Anterior", max_length=12,null=True, blank=True)
    nombre = models.CharField("Nombre",max_length=200,null=True,blank=True)
    nombre_adi = models.CharField("Nombre ADI",max_length=200,null=True,blank=True)
    numero_region = models.IntegerField("Numero Region", null=True, blank=True)
    pais = models.CharField("Pais",max_length=50,null=True,blank=True)
    parte = models.IntegerField("Parte",null=True,blank=True)
    primer_descriptor_sectorial =models.CharField("Primer descriptor sectorial",max_length=200,null=True,blank=True)
    proceso = models.CharField("Proceso",max_length=20,null=True,blank=True)
    provincia = models.CharField("Provincia",max_length=50,null=True,blank=True)
    region = models.CharField("Región",max_length=100,null=True,blank=True)
    sector = models.CharField("Sector",max_length=50,null=True,blank=True)
    segundo_descriptor_sectorial = models.CharField("Segundo Descriptor Sectorial",max_length=200,null=True,blank=True)
    subsector = models.CharField("Subsector",max_length=200,null=True,blank=True)
    tercer_descriptor_sectorial = models.CharField("Tercer Descriptor Sectorial",max_length=200,null=True,blank=True)
    tiene_adi = models.CharField("Tiene ADI",max_length=5,null=True,blank=True)
    tipologia = models.CharField("Tipologia",max_length=20,null=True,blank=True)

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.codigo_bip, self.nombre, self.sector, self.subsector)
