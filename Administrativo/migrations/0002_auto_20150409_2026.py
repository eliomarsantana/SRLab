# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='EstadoFuncional',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='UsoDoLaboratorio',
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
        migrations.DeleteModel(
            name='Reserva_Estado_Uso_Lab',
        ),
        migrations.DeleteModel(
            name='Reserva_Uso_Lab',
        ),
    ]
