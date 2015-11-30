# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0004_auto_20151127_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicemodel',
            name='modelImg',
            field=models.ImageField(null=True, upload_to=b'img/indexModel', blank=True),
        ),
    ]
