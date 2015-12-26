# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpub', '0039_article_usernickname'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lession',
            new_name='Lesson',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='lessionname',
            new_name='lessonname',
        ),
    ]
