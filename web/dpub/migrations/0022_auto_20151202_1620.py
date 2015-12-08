# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dpub', '0021_exuser_identity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('img', models.ImageField(help_text=b'\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe\xe5\x83\x8f', null=True, upload_to=b'img/article/')),
                ('contactinformation', models.CharField(help_text=b'\xe8\x81\x94\xe7\xb3\xbb\xe6\x96\xb9\xe5\xbc\x8f', max_length=20)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='modelImg',
            field=models.ImageField(null=True, upload_to=b'img/indexModel/', blank=True),
        ),
    ]
