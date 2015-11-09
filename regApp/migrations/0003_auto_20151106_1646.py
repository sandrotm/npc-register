# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regApp', '0002_auto_20151105_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='fb_id',
            field=models.CharField(max_length=190, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='position',
            field=models.CharField(max_length=190, default='none', verbose_name='თანამდებობა'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='workplace',
            field=models.CharField(max_length=190, default='none', verbose_name='სამუშაო ადგილი'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='district',
            field=models.ForeignKey(to='regApp.District', verbose_name='რაიონი / რეგიონი'),
        ),
    ]
