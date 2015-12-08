# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0027_auto_20151203_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='classify',
            field=models.ForeignKey(default=1, to='dpub.ClassModel'),
            preserve_default=False,
        ),
    ]
