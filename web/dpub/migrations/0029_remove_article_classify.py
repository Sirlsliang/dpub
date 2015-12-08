# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0028_auto_20151203_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='classify',
        ),
    ]
