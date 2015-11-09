# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regApp', '0003_auto_20151106_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(verbose_name='ელ-ფოსტა', null=True, max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='fb_id',
            field=models.CharField(null=True, max_length=190, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='position',
            field=models.CharField(verbose_name='თანამდებობა', null=True, max_length=190, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='workplace',
            field=models.CharField(verbose_name='სამუშაო ადგილი', null=True, max_length=190, blank=True),
        ),
    ]
