# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0002_auto_20151014_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arauco',
            name='fech_cmand',
            field=models.DateField(null=True, blank=True),
        ),
    ]
