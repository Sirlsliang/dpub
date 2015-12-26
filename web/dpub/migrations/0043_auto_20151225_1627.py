# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0042_auto_20151222_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='school',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='School',
        ),
    ]
