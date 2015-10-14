# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0002_auto_20150505_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inversion',
            name='ano_postul',
            field=models.IntegerField(null=True, verbose_name=b'Ano postulacion', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='cod_comu',
            field=models.IntegerField(null=True, verbose_name=b'Codigo comuna', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='cod_corr',
            field=models.IntegerField(null=True, verbose_name=b'Codigo Corr', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='cod_estado',
            field=models.IntegerField(null=True, verbose_name=b'Codigo Estado', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='cod_proy_ugit',
            field=models.IntegerField(null=True, verbose_name=b'Codigo Proyecto UGIT', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='id_bip_n',
            field=models.IntegerField(null=True, verbose_name=b'Codigo BIP numero', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='mont_pesos',
            field=models.IntegerField(null=True, verbose_name=b'Monto pesos', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='n_cert_core',
            field=models.CharField(max_length=4, null=True, verbose_name=b'Numero certificado CORE', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='n_ses_core',
            field=models.IntegerField(null=True, verbose_name=b'Numero sersion CORE', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='obs1',
            field=models.IntegerField(null=True, verbose_name=b'OBS 1', blank=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='situacion',
            field=models.IntegerField(null=True, verbose_name=b'Situacion', blank=True),
        ),
    ]
