# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0041_auto_20151221_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='server',
            field=models.ForeignKey(related_name='lessonModel', to='dpub.Servers'),
        ),
    ]
