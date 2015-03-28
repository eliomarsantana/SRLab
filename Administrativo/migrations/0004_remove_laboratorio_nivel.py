# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0003_auto_20150323_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratorio',
            name='Nivel',
        ),
    ]
