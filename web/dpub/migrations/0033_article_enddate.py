# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0032_auto_20151204_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 4, 12, 49, 29, 634844, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
