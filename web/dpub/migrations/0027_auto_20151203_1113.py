# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0026_auto_20151203_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='contactinformation',
        ),
        migrations.AddField(
            model_name='article',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='phonenum',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
