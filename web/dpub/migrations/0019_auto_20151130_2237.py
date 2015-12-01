# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0018_auto_20151130_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exuser',
            name='identity',
            field=models.CharField(max_length=2),
        ),
    ]
