# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0030_article_classify'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('companyname', models.CharField(max_length=50, null=True, blank=True)),
                ('companyadd', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='exuser',
            name='company',
            field=models.ForeignKey(blank=True, to='dpub.Company', null=True),
        ),
    ]
