# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regApp', '0004_auto_20151106_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='district',
            field=models.CharField(verbose_name='რაიონი / რეგიონი', max_length=95),
        ),
    ]
