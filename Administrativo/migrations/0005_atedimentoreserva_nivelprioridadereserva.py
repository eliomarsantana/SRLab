# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0004_estadolaboratorio_usolaboratorio'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtedimentoReserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Atendida', models.TextField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NivelPrioridadeReserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nivel', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
