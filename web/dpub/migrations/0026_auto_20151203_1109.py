# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0025_exuser_tel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exuser',
            old_name='tel',
            new_name='phonenum',
        ),
        migrations.AddField(
            model_name='article',
            name='classify',
            field=models.ForeignKey(blank=True, to='dpub.ClassModel', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='company',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='insertDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 3, 9, 5, 558516, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exuser',
            name='headimg',
            field=models.ImageField(null=True, upload_to=b'img/headphoto/', blank=True),
        ),
        migrations.AddField(
            model_name='exuser',
            name='nickname',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='exuser',
            name='sex',
            field=models.CharField(default=b'0', max_length=2, null=True, blank=True, choices=[(b'0', b'\xe7\x94\xb7'), (b'1', b'\xe5\xa5\xb3')]),
        ),
    ]
