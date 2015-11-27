# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('courName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schName', models.CharField(max_length=100)),
                ('schDesc', models.TextField()),
                ('schUrl', models.URLField()),
                ('schLogo', models.ImageField(upload_to=b'schoolLogo/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userName', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('inTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='scholl',
            field=models.ForeignKey(to='dpub.School'),
        ),
    ]
