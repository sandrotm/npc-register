# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=95)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(max_length=95)),
                ('last_name', models.CharField(max_length=95)),
                ('personal_id', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('settlement', models.CharField(max_length=95)),
                ('address', models.CharField(max_length=190)),
                ('birth_date', models.DateField()),
                ('sex', models.CharField(choices=[('male', 'მამრობითი'), ('female', 'მდედრობითი')], max_length=15)),
                ('district', models.ForeignKey(to='regApp.District')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('value', models.CharField(max_length=15)),
                ('type', models.CharField(choices=[('mobile', 'მობილური'), ('home', 'სახლის'), ('work', 'სამსახურის')], max_length=12)),
                ('person', models.ForeignKey(to='regApp.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=95)),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(to='regApp.Region'),
        ),
    ]
