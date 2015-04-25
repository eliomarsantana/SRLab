# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0017_pacotelaboratorio_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwareReservaLab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Data_da_Solicitacao', models.DateField()),
                ('Horario_Solicitacao', models.TimeField()),
                ('reserva', models.ForeignKey(to='Administrativo.Reserva')),
                ('software', models.ForeignKey(to='Administrativo.Software')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='pacotelaboratorio',
            name='Reserva',
        ),
    ]
