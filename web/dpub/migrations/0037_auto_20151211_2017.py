# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0036_auto_20151210_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exuser',
            name='identity',
        ),
        migrations.AlterField(
            model_name='exuser',
            name='phonenum',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
