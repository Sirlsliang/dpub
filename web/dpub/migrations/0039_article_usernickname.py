# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0038_auto_20151212_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='usernickname',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
