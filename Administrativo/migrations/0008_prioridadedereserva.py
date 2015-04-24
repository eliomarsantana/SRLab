# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0007_auto_20150422_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrioridadeDeReserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Data_Autorizacao', models.DateField()),
                ('Data_Atendimento_da_Reserva', models.DateField()),
                ('Hora_Autorizacao', models.TimeField()),
                ('Prioridade', models.ForeignKey(to='Administrativo.NivelPrioridadeReserva')),
                ('Reserva', models.ForeignKey(to='Administrativo.Reserva')),
                ('Reserva_Atendida', models.ForeignKey(to='Administrativo.AtedimentoReserva')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
