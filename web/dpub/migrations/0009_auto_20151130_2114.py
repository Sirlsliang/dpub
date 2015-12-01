# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0008_auto_20151130_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exuser',
            name='identity',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'1', b'Company'), (b'0', b'Student')]),
        ),
    ]
