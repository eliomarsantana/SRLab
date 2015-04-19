# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Computadores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Quantidad_de_Memoria', models.IntegerField()),
                ('Frequencia_do_Processador', models.CharField(max_length=20)),
                ('Presenca_de_CD_Disquete', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Numero_de_Maquinas', models.IntegerField()),
                ('Lotacao_Maxima', models.IntegerField()),
                ('Aula', models.ForeignKey(to='Administrativo.Aula')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nivel', models.CharField(max_length=60)),
                ('Predio', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PacoteDeSoftware',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pacote', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=60)),
                ('versao', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=100)),
                ('Pacote', models.ForeignKey(to='Administrativo.PacoteDeSoftware')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoUso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_de_uso', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='Locais',
            field=models.ForeignKey(to='Administrativo.Localizacao'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='Tipo_De_Uso',
            field=models.ForeignKey(to='Administrativo.TipoUso'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computadores',
            name='Laboratorio',
            field=models.ForeignKey(to='Administrativo.Laboratorio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computadores',
            name='Pacotes',
            field=models.ManyToManyField(to='Administrativo.PacoteDeSoftware'),
            preserve_default=True,
        ),
    ]
