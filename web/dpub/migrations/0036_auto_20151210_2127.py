# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0035_auto_20151210_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exuser',
            name='sex',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, b'\xe7\x94\xb7'), (1, b'\xe5\xa5\xb3')]),
        ),
    ]
