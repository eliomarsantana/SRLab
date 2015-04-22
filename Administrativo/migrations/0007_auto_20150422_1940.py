# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0006_estadolaboratorioreserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Data_da_Reserva', models.DateTimeField()),
                ('Uso_Internet', models.CharField(max_length=1)),
                ('Laboratorio', models.ForeignKey(to='Administrativo.Laboratorio')),
                ('Tipo_Aula', models.ForeignKey(to='Administrativo.Aula')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='estadolaboratorioreserva',
            name='Laboratorio_Reserva',
            field=models.ForeignKey(default=1, to='Administrativo.Reserva'),
            preserve_default=False,
        ),
    ]
