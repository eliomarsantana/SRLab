# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0002_auto_20150322_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDeUso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_de_uso', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='computadores',
            old_name='frequenciaProcessador',
            new_name='Frequencia_do_Processador',
        ),
        migrations.RenameField(
            model_name='computadores',
            old_name='quantidadeDeMemoriaDisp',
            new_name='Quantidad_de_Memoria',
        ),
        migrations.RemoveField(
            model_name='computadores',
            name='presencaDeUniCdDisquete',
        ),
        migrations.AddField(
            model_name='computadores',
            name='Presenca_de_CD_Disquete',
            field=models.CharField(default='sim', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='Tipo_DeUso',
            field=models.ForeignKey(to='Administrativo.TipoDeUso'),
            preserve_default=True,
        ),
    ]
