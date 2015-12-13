# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0037_auto_20151211_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='classify',
            new_name='classmodel',
        ),
        migrations.AddField(
            model_name='article',
            name='servicemodel',
            field=models.ForeignKey(default=1, to='dpub.ServiceModel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='phonenum',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
