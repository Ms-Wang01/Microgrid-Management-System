# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microgrids', '0002_auto_20180620_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batterydata',
            options={'verbose_name': '蓄电池数据', 'verbose_name_plural': '蓄电池数据'},
        ),
        migrations.AlterModelOptions(
            name='batteryproperty',
            options={'verbose_name': '蓄电池属性', 'verbose_name_plural': '蓄电池属性'},
        ),
        migrations.AddField(
            model_name='batteryproperty',
            name='battery_num',
            field=models.CharField(default=1, max_length=20, unique=True, verbose_name='电池编号'),
            preserve_default=False,
        ),
    ]
