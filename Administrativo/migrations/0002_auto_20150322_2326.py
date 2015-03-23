# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laboratorio',
            old_name='localizacaoNivel',
            new_name='Lotacao_Maxima',
        ),
        migrations.RenameField(
            model_name='laboratorio',
            old_name='lotacaoMaxima',
            new_name='Nivel',
        ),
        migrations.RenameField(
            model_name='laboratorio',
            old_name='numeroDeMaquinasDisp',
            new_name='Numero_de_Maquinas',
        ),
        migrations.RenameField(
            model_name='laboratorio',
            old_name='localizacaoPredio',
            new_name='Predio',
        ),
        migrations.RenameField(
            model_name='laboratorio',
            old_name='TipoDeUso',
            new_name='Tipo_DeUso',
        ),
    ]
