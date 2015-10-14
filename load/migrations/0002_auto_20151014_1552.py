# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arauco',
            name='fecha_cer',
            field=models.CharField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='arauco',
            name='fecha_cert',
            field=models.DateField(null=True, blank=True),
        ),
    ]
