# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0031_auto_20151204_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='company',
            new_name='companyname',
        ),
        migrations.RemoveField(
            model_name='exuser',
            name='company',
        ),
        migrations.AddField(
            model_name='exuser',
            name='companyname',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
