# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0008_prioridadedereserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nivelprioridadereserva',
            name='Nivel',
            field=models.TextField(max_length=1),
            preserve_default=True,
        ),
    ]
