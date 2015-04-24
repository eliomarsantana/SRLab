# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0014_reserva_uso_internet'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='Horario_Reserva',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='Data_da_Reserva',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
