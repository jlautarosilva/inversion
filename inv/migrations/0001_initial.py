# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inversion',
            fields=[
                ('num_corr', models.AutoField(serialize=False, primary_key=True)),
                ('ano_postul', models.IntegerField(verbose_name=b'in_value=1, max_value=9999')),
                ('situacion', models.IntegerField(verbose_name=b'in_value=0, max_value=9')),
                ('id_bip_n', models.IntegerField(verbose_name=b'in_value=10000000, max_value=99999999')),
                ('id_bip_t', models.CharField(max_length=8, verbose_name=b'Codigo BIP texto')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('obs1', models.IntegerField(verbose_name=b'in_value=0, max_value=99')),
                ('cod_comu', models.IntegerField(verbose_name=b'in_value=0, max_value=9999')),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
