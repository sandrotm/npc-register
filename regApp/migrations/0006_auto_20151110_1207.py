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
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'წევრი'},
        ),
        migrations.AddField(
            model_name='member',
            name='email_confirm',
            field=models.CharField(max_length=95, default='fail', choices=[('fail', 'ვერ გაიგზავნა'), ('unconfirmed', 'გაიგზავნა, მაგრამ არ დაუდასტურებია'), ('confirmed', 'დაადასტურა')]),
        ),
        migrations.AddField(
            model_name='member',
            name='member_confirm_id',
            field=models.CharField(null=True, blank=True, unique=True, verbose_name='წევრის უნიკალური იდენტიფიკატორი', max_length=40),
        ),
        migrations.AddField(
            model_name='member',
            name='sex',
            field=models.CharField(null=True, blank=True, max_length=15, default='unknown', choices=[('unknown', 'უცნობი'), ('male', 'მამრობითი'), ('female', 'მდედრობითი'), ('other', 'სხვა')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(verbose_name='ელ-ფოსტა', max_length=254),
        ),
        migrations.AlterField(
            model_name='member',
            name='personal_id',
            field=models.CharField(unique=True, verbose_name='პირადი ნომერი', max_length=12),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(null=True, blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_type',
            field=models.CharField(max_length=12, default='mobile', choices=[('mobile', 'მობილური'), ('home', 'სახლის'), ('work', 'სამსახურის')]),
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]
