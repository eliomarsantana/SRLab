# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0008_locais_nivel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TipoDeUso',
            new_name='TipoLaboratorio',
        ),
        migrations.RenameField(
            model_name='laboratorio',
            old_name='Tipo_DeUso',
            new_name='Tipo_De_Uso',
        ),
    ]
