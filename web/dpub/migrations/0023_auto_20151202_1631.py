# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0022_auto_20151202_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(help_text=b'\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe\xe5\x83\x8f', null=True, upload_to=b'img/article/', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
