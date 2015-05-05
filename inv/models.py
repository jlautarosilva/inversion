from django.contrib.gis.db import models

#Implementar validadores para los integerfield
from django.core.validators import MinValueValidator, MaxValueValidator

class inversion(models.Model):

    num_corr = models.AutoField(primary_key=True)
    ano_postul = models.IntegerField("in_value=1, max_value=9999")
    situacion = models.IntegerField("in_value=0, max_value=9")
    id_bip_n = models.IntegerField("in_value=10000000, max_value=99999999")
    id_bip_t = models.CharField('Codigo BIP texto',max_length=8)
    x = models.DecimalField(max_digits = 6, decimal_places = 3)
    y = models.DecimalField(max_digits = 7, decimal_places = 6)
    obs1 = models.IntegerField("in_value=0, max_value=99")
    cod_comu = models.IntegerField("in_value=0, max_value=9999")
    cod_corr = models.IntegerField("5")
    cod_estado = models.IntegerField("2")
    estado_postu = models.CharField('Estado de la Postulacion', max_length=18)
    cod_proy_ugit = models.IntegerField('18')
    rep_conadi = models.CharField('Rep CONADI', max_length=9)
    nom_proy = models.CharField('Nombre del Proyecto',999)
    n_cert_core = models.CharField('\\abc', max_length=4)
    n_ses_core = models.IntegerField('4')
    fec_core = models.DateField()
    mont_pesos = models.IntegerField()
    fuen_finan = models.CharField(max_length=30)
    comuna = models.CharField(max_length=20)
    provincia = models.CharField(max_length=10)
    terr_planif = models.CharField(max_length=20)
    glosa = models.CharField(max_length=999)
    tipologias = models.CharField(max_length=20)
    sector = models.CharField(max_length=20)
    sec_terr_com = models.CharField(max_length=999)
    rate = models.CharField(max_length=2)
    fec_rate = models.DateField()


    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    def __str__(self):
        return self.name
