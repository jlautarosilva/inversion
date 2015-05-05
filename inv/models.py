from django.contrib.gis.db import models

#Implementar validadores para los integerfield
from django.core.validators import MinValueValidator, MaxValueValidator

class inversion(models.Model):

    num_corr = models.AutoField(primary_key=True)
    ano_postul = models.IntegerField("in_value=1, max_value=9999",null=True, blank=True)
    situacion = models.IntegerField("in_value=0, max_value=9",null=True, blank=True)
    id_bip_n = models.IntegerField("in_value=10000000, max_value=99999999",null=True, blank=True)
    id_bip_t = models.CharField('Codigo BIP texto',max_length=8,null=True, blank=True)
    x = models.DecimalField(max_digits = 6, decimal_places = 3,null=True, blank=True)
    y = models.DecimalField(max_digits = 7, decimal_places = 6,null=True, blank=True)
    obs1 = models.IntegerField("in_value=0, max_value=99",null=True, blank=True)
    cod_comu = models.IntegerField("in_value=0, max_value=9999",null=True, blank=True)
    cod_corr = models.IntegerField(" max 5",null=True, blank=True)
    cod_estado = models.IntegerField("max 2",null=True, blank=True)
    estado_postu = models.CharField('Estado de la Postulacion', max_length=18,null=True, blank=True)
    cod_proy_ugit = models.IntegerField('max 18',null=True, blank=True)
    rep_conadi = models.CharField('Rep CONADI', max_length=9,null=True, blank=True)
    nom_proy = models.CharField('Nombre del Proyecto',max_length=999,null=True, blank=True)
    n_cert_core = models.CharField('abc', max_length=4,null=True, blank=True)
    n_ses_core = models.IntegerField('max4',null=True, blank=True)
    fec_core = models.DateField(null=True, blank=True)
    mont_pesos = models.IntegerField('max 12',null=True, blank=True)
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
