# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0011_auto_20150422_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='Uso_Internet',
            field=models.BooleanField(verbose_name=True),
            preserve_default=True,
        ),
    ]
