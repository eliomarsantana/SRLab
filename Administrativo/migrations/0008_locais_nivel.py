# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0007_niveis'),
    ]

    operations = [
        migrations.AddField(
            model_name='locais',
            name='nivel',
            field=models.ForeignKey(default=1, to='Administrativo.Niveis'),
            preserve_default=False,
        ),
    ]
