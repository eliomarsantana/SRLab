# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0002_reservanaoatendida'),
    ]

    operations = [
        migrations.CreateModel(
            name='PacoteLaboratorio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Data_Solicitacao', models.DateField()),
                ('Hora_Solicitacao', models.TimeField()),
                ('Laboratorio', models.ForeignKey(to='Administrativo.Laboratorio')),
                ('Pacotes', models.ForeignKey(to='Administrativo.PacoteDeSoftware')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='ReservaNaoAtendida',
        ),
    ]
