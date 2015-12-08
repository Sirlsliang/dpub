# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0024_auto_20151202_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='exuser',
            name='tel',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
