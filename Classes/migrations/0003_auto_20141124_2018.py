# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0002_permissao_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissao',
            name='HoraSaida',
            field=models.DateTimeField(verbose_name=b'Hora de Sa\xc3\xadda', blank=True),
        ),
    ]
