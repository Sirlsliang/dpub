# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0040_auto_20151221_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='serverbanner',
            field=models.ImageField(null=True, upload_to=b'img/serverbanner/', blank=True),
        ),
        migrations.AlterField(
            model_name='servers',
            name='serverlogo',
            field=models.ImageField(null=True, upload_to=b'img/serverlogo/', blank=True),
        ),
    ]
