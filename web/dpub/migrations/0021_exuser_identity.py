# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0020_remove_exuser_identity'),
    ]

    operations = [
        migrations.AddField(
            model_name='exuser',
            name='identity',
            field=models.CharField(default=b'1', max_length=2, choices=[(b'0', b'\xe4\xbc\x81\xe4\xb8\x9a'), (b'1', b'\xe5\xad\xa6\xe7\x94\x9f')]),
        ),
    ]
