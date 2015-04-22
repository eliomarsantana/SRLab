# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaNaoAtendida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Numero_Laboratorio', models.IntegerField()),
                ('Data', models.DateTimeField()),
                ('Usuario', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
