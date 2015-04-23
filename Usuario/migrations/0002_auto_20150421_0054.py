# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='Laboratorio',
            field=models.ForeignKey(to='Administrativo.Laboratorio'),
            preserve_default=True,
        ),
    ]
