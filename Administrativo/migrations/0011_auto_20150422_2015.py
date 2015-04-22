# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0010_auto_20150422_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nivelprioridadereserva',
            name='Nivel',
            field=models.CharField(max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='Email',
            field=models.CharField(max_length=60),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='Nome_Usuario',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='Uso_Internet',
            field=models.BooleanField(),
            preserve_default=True,
        ),
    ]
