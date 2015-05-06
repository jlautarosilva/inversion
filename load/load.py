# -*- coding: utf-8 -*-
import os
from django.contrib.gis.utils import LayerMapping
from models import Arauco

arauco_mapping = {
    'id' : 'ID',
    'fech_plani' : 'FECH_PLANI',
    'respon_eje' : 'RESPON_EJE',
    'codigo_bip' : 'CODIGO_BIP',
    'x' : 'X',
    'y' : 'Y',
    'nombre' : 'NOMBRE',
    'iniciativa' : 'INICIATIVA',
    'comuna' : 'COMUNA',
    'etapa_post' : 'ETAPA_POST',
    'sector' : 'SECTOR',
    'area' : 'AREA',
    'cos_totm_field' : 'COS_TOTM_',
    'financiera' : 'FINANCIERA',
    'glosa_conv' : 'GLOSA_CONV',
    'rezago_mop' : 'REZAGO_MOP',
    'rate' : 'RATE',
    'fecha_rate' : 'FECHA_RATE',
    'n_cer_core' : 'N_CER_CORE',
    'fecha_cer' : 'FECHA__CER',
    'situacion' : 'SITUACION',
    'tipologia' : 'TIPOLOGIA',
    'meca_finan' : 'MECA_FINAN',
    'cartera' : 'CARTERA',
    'exitos' : 'EXITOS',
    'temporalid' : 'TEMPORALID',
    '_2014' : '2014',
    '_2015' : '2015',
    '_2016' : '2016',
    '_2017' : '2017',
    '_2018' : '2018',
    '_2019' : '2019',
    '_2020' : '2020',
    '_2021' : '2021',
    '_2022' : '2022',
    '_2023' : '2023',
    'n_corr_ugi' : 'N_CORR_UGI',
#    'ano_presen' : 'AÑO_PRESEN',
#    'ano_presup' : 'AÑO_PRESUP',
    'ano_presen' : 'AO_PRESEN',
    'ano_presup' : 'AO_PRESUP',
    'cod_bip' : 'COD_BIP',
    'nombre_del' : 'NOMBRE_DEL',
    'comuna_1' : 'COMUNA_1',
    'provincia' : 'PROVINCIA',
    'certif_co' : 'CERTIF__CO',
    'fecha_cert' : 'FECHA_CERT',
    'tipologias' : 'TIPOLOGIAS',
    'unidad_tec' : 'UNIDAD_TEC',
    'subtit_ulo' : 'SUBTIT_ULO',
    'items' : 'ITEMS',
    'asignacion' : 'ASIGNACION',
    'resolucion' : 'RESOLUCION',
    'fech_cmand' : 'FECH_CMAND',
    'monto_cman' : 'MONTO_CMAN',
    'geom' : 'MULTIPOINT',
}

arauco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/SHP/Arauco_corregido_utf-8.shp'))

def run(verbose=True):
    lm = LayerMapping(Arauco, arauco_shp, arauco_mapping, transform=False, encoding='utf-8')
    lm.save(strict=True, verbose=verbose)
