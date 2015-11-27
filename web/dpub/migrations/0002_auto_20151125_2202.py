# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='schLogo',
            field=models.ImageField(upload_to=b'img/schoolLogo/'),
        ),
    ]
