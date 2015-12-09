# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0033_article_enddate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-insertDate']},
        ),
        migrations.AddField(
            model_name='article',
            name='boolIndex',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
