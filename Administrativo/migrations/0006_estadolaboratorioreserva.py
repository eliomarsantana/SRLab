# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0005_atedimentoreserva_nivelprioridadereserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoLaboratorioReserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Estado_Laboratorio', models.ForeignKey(to='Administrativo.EstadoLaboratorio')),
                ('Laboratorio', models.ForeignKey(to='Administrativo.Laboratorio')),
                ('Uso_Laboratorio', models.ForeignKey(to='Administrativo.UsoLaboratorio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
