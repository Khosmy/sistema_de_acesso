# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0004_auto_20141124_2019'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='permissao',
            unique_together=set([('Local', 'Pessoa')]),
        ),
    ]
