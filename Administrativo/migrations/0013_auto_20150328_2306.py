# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0012_reserva_data_da_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva_Estado_Uso_Lab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reserva_Uso_Lab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='EstadoFuncional',
            field=models.ForeignKey(to='Administrativo.Reserva_Estado_Uso_Lab'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='UsoDoLaboratorio',
            field=models.ForeignKey(to='Administrativo.Reserva_Uso_Lab'),
            preserve_default=True,
        ),
    ]
