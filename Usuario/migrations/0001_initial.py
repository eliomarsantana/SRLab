# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0002_auto_20150409_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Data_da_Reserva', models.DateTimeField()),
                ('Uso_Internet', models.CharField(max_length=1)),
                ('Laboratorio', models.OneToOneField(to='Administrativo.Laboratorio')),
                ('Pacotes', models.ManyToManyField(to='Administrativo.PacoteDeSoftware')),
                ('Tipo_Aula', models.ForeignKey(to='Administrativo.Aula')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
