# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import dpub.myValidator


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0045_auto_20151225_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exuser',
            name='boolServer',
            field=models.NullBooleanField(help_text=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86'),
        ),
        migrations.AlterField(
            model_name='exuser',
            name='companyname',
            field=models.CharField(help_text=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='exuser',
            name='headimg',
            field=models.ImageField(help_text=b'\xe5\xa4\xb4\xe5\x83\x8f', null=True, upload_to=b'img/headphoto/', blank=True),
        ),
        migrations.AlterField(
            model_name='exuser',
            name='inTime',
            field=models.DateTimeField(help_text=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', auto_now=True),
        ),
        migrations.AlterField(
            model_name='exuser',
            name='nickname',
            field=models.CharField(help_text=b'\xe6\x98\xb5\xe7\xa7\xb0', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='exuser',
            name='phonenum',
            field=models.CharField(blank=True, max_length=15, null=True, help_text=b'\xe7\x94\xb5\xe8\xaf\x9d\xe5\x8f\xb7\xe7\xa0\x81', validators=[dpub.myValidator.vald_phonenum]),
        ),
        migrations.AlterField(
            model_name='exuser',
            name='server',
            field=models.OneToOneField(null=True, blank=True, to='dpub.Servers', help_text=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='exuser',
            name='sex',
            field=models.IntegerField(default=0, help_text=b'\xe6\x80\xa7\xe5\x88\xab', null=True, blank=True, choices=[(0, b'\xe7\x94\xb7'), (1, b'\xe5\xa5\xb3')]),
        ),
        migrations.AlterField(
            model_name='servers',
            name='serverdesc',
            field=models.TextField(help_text=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe7\xae\x80\xe4\xbb\x8b'),
        ),
        migrations.AlterField(
            model_name='servers',
            name='servername',
            field=models.CharField(help_text=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe5\x90\x8d\xe7\xa7\xb0', max_length=100),
        ),
    ]
