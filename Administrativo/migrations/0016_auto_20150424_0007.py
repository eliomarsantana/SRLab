# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0015_auto_20150424_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='Horario_Reserva',
            field=models.TimeField(),
            preserve_default=True,
        ),
    ]
