# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0010_auto_20151130_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exuser',
            name='identity',
            field=models.CharField(default=b'\xe5\xad\xa6\xe7\x94\x9f', max_length=2, choices=[(b'1', b'\xe4\xbc\x81\xe4\xb8\x9a'), (b'0', b'\xe5\xad\xa6\xe7\x94\x9f')]),
        ),
    ]
