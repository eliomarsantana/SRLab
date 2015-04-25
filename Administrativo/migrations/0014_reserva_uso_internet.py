# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0013_auto_20150423_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='Uso_Internet',
            field=models.ForeignKey(default=1, to='Administrativo.UsoInternet'),
            preserve_default=False,
        ),
    ]
