# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0005_servicemodel_modelimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classmodel',
            name='modelName',
            field=models.ForeignKey(related_name='classModel', to='dpub.ServiceModel'),
        ),
    ]
