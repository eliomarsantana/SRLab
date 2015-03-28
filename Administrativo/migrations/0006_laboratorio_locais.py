# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0005_locais'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratorio',
            name='Locais',
            field=models.ForeignKey(default=1, to='Administrativo.Locais'),
            preserve_default=False,
        ),
    ]
