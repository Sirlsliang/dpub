# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0019_auto_20151130_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exuser',
            name='identity',
        ),
    ]
