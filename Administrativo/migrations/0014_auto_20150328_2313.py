# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0013_auto_20150328_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva_estado_uso_lab',
            old_name='descricao',
            new_name='situacao',
        ),
        migrations.RenameField(
            model_name='reserva_uso_lab',
            old_name='descricao',
            new_name='uso',
        ),
    ]
