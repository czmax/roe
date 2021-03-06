# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-29 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CMDB', '0022_mysql_user_memo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysql_instance',
            name='db_status',
            field=models.CharField(blank=True, choices=[('\u670d\u52a1\u4e2d', '\u670d\u52a1\u4e2d'), ('\u4ec5\u4ece\u5e93', '\u4ec5\u4ece\u5e93'), ('\u6545\u969c', '\u6545\u969c'), ('\u5176\u4ed6', '\u5176\u4ed6')], max_length=30, null=True, verbose_name='DB\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='mysql_instance',
            name='dbcluster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mysql_instance', to='CMDB.MySQLCluster'),
        ),
        migrations.AlterField(
            model_name='mysql_instance',
            name='dbtag',
            field=models.CharField(max_length=50, verbose_name='\u6570\u636e\u5e93\u5b9e\u4f8b\u6807\u7b7e'),
        ),
        migrations.AlterUniqueTogether(
            name='mysql_instance',
            unique_together=set([('m_ip', 'port')]),
        ),
    ]
