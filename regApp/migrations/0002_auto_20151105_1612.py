# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='person',
        ),
        migrations.RemoveField(
            model_name='member',
            name='sex',
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=15, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='phone_type',
            field=models.CharField(max_length=12, choices=[('mobile', 'მობილური'), ('home', 'სახლის'), ('work', 'სამსახურის')], default='mobile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(max_length=190, verbose_name='მისამართი'),
        ),
        migrations.AlterField(
            model_name='member',
            name='birth_date',
            field=models.DateField(verbose_name='დაბადების თარიღი'),
        ),
        migrations.AlterField(
            model_name='member',
            name='district',
            field=models.ForeignKey(to='regApp.District', verbose_name='რაიონი'),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ელ-ფოსტა'),
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=95, verbose_name='სახელი'),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(max_length=95, verbose_name='გვარი'),
        ),
        migrations.AlterField(
            model_name='member',
            name='personal_id',
            field=models.CharField(max_length=12, verbose_name='პირადი ნომერი'),
        ),
        migrations.AlterField(
            model_name='member',
            name='settlement',
            field=models.CharField(max_length=95, verbose_name='ქალაქი ან სოფელი'),
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
    ]
