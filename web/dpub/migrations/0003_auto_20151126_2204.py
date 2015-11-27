# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0002_auto_20151125_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='scholl',
            new_name='school',
        ),
    ]
