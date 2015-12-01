# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0016_auto_20151130_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exuser',
            name='identity',
            field=models.IntegerField(max_length=2, null=True, choices=[(1, b'\xe4\xbc\x81\xe4\xb8\x9a'), (0, b'\xe5\xad\xa6\xe7\x94\x9f')]),
        ),
    ]
