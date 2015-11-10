# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regApp', '0005_auto_20151106_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='region',
        ),
        migrations.AddField(
            model_name='member',
            name='email_confirm',
            field=models.CharField(choices=[('fail', 'ვერ გაიგზავნა'), ('unconfirmed', 'გაიგზავნა, მაგრამ არ დაუდასტურებია'), ('confirmed', 'დაადასტურა')], max_length=95, default='fail'),
        ),
        migrations.AddField(
            model_name='member',
            name='member_id',
            field=models.CharField(max_length=12, verbose_name='წევრის უნიკალური იდენტიფიკატორი', unique=True, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='sex',
            field=models.CharField(choices=[('unknown', 'უცნობი'), ('male', 'მამრობითი'), ('female', 'მდედრობითი'), ('other', 'სხვა')], max_length=15, default='unknown'),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(verbose_name='ელ-ფოსტა', max_length=254, default='noemail@noemail.com'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=15, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_type',
            field=models.CharField(choices=[('mobile', 'მობილური'), ('home', 'სახლის'), ('work', 'სამსახურის')], max_length=12, default='mobile'),
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]
