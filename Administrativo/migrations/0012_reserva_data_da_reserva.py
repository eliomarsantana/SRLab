# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0011_software_pacote'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='Data_da_Reserva',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 21, 0, 54, 435000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
