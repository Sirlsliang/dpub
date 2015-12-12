# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0034_auto_20151208_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lessionname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('servername', models.CharField(max_length=100)),
                ('serverdesc', models.TextField()),
                ('serverurl', models.URLField()),
                ('serverlogo', models.ImageField(upload_to=b'img/serverlogo/')),
                ('serverbanner', models.ImageField(upload_to=b'img/serverbanner/')),
                ('serverclass', models.CharField(default=b'0', max_length=2, choices=[(b'0', b'\xe4\xb8\xaa\xe4\xba\xba\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86'), (b'1', b'\xe4\xbc\x81\xe4\xb8\x9a\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86'), (b'2', b'\xe6\xa0\xa1\xe5\x9b\xad\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86')])),
                ('servertel', models.CharField(max_length=12, null=True, blank=True)),
                ('serveraddress', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='exuser',
            name='boolServer',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='lession',
            name='server',
            field=models.ForeignKey(to='dpub.Servers'),
        ),
        migrations.AddField(
            model_name='exuser',
            name='server',
            field=models.OneToOneField(null=True, blank=True, to='dpub.Servers'),
        ),
    ]
