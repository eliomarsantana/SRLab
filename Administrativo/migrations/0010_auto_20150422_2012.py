# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0009_auto_20150422_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='Email',
            field=models.TextField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='Nome_Usuario',
            field=models.TextField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
