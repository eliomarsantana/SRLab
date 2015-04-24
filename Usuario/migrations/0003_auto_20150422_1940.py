# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0002_auto_20150421_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='Laboratorio',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='Pacotes',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='Tipo_Aula',
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
    ]
