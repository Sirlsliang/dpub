# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0043_auto_20151225_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='boolWorks',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'\xe9\x9c\x80\xe6\xb1\x82'), (b'1', b'\xe4\xbd\x9c\xe5\x93\x81')]),
        ),
    ]
