# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0044_article_boolworks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='endDate',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='price',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
