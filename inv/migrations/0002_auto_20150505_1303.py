# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inversion',
            name='cod_corr',
            field=models.IntegerField(null=True, verbose_name=b' max 5', blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='cod_estado',
            field=models.IntegerField(null=True, verbose_name=b'max 2', blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='cod_proy_ugit',
            field=models.IntegerField(null=True, verbose_name=b'max 18', blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='comuna',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='estado_postu',
            field=models.CharField(max_length=18, null=True, verbose_name=b'Estado de la Postulacion', blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='fec_core',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='fec_rate',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='fuen_finan',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='glosa',
            field=models.CharField(max_length=999, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='mont_pesos',
            field=models.IntegerField(null=True, verbose_name=b'max 12', blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='n_cert_core',
            field=models.CharField(max_length=4, null=True, verbose_name=b'abc', blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='n_ses_core',
            field=models.IntegerField(null=True, verbose_name=b'max4', blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='nom_proy',
            field=models.CharField(max_length=999, null=True, verbose_name=b'Nombre del Proyecto', blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='provincia',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='rate',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='rep_conadi',
            field=models.CharField(max_length=9, null=True, verbose_name=b'Rep CONADI', blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='sec_terr_com',
            field=models.CharField(max_length=999, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='sector',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='terr_planif',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inversion',
            name='tipologias',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='ano_postul',
            field=models.IntegerField(null=True, verbose_name=b'in_value=1, max_value=9999', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='cod_comu',
            field=models.IntegerField(null=True, verbose_name=b'in_value=0, max_value=9999', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='id_bip_n',
            field=models.IntegerField(null=True, verbose_name=b'in_value=10000000, max_value=99999999', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='id_bip_t',
            field=models.CharField(max_length=8, null=True, verbose_name=b'Codigo BIP texto', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='obs1',
            field=models.IntegerField(null=True, verbose_name=b'in_value=0, max_value=99', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='situacion',
            field=models.IntegerField(null=True, verbose_name=b'in_value=0, max_value=9', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='x',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=3, blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='y',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=6, blank=True),
        ),
    ]
