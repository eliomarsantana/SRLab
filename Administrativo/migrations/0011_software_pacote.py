# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0010_pacotedesoftware'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='Pacote',
            field=models.ForeignKey(default=1, to='Administrativo.PacoteDeSoftware'),
            preserve_default=False,
        ),
    ]
