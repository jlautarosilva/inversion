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

    def __str__(self):
        return self.name

#class convenio (models.Model):
#    id_bip_t = models.Fo
