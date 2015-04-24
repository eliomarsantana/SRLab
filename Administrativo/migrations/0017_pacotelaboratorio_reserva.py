# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0016_auto_20150424_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacotelaboratorio',
            name='Reserva',
            field=models.ForeignKey(default=1, to='Administrativo.Reserva'),
            preserve_default=False,
        ),
    ]
