# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='app_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='cmd_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('com', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Host_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('h_name', models.CharField(max_length=50, null=True, blank=True)),
                ('h_user', models.CharField(default=b'root', max_length=20, null=True, blank=True)),
                ('h_pass', models.CharField(max_length=30)),
                ('h_mx', models.TextField(null=True, blank=True)),
                ('h_cpu', models.CharField(max_length=20, blank=True)),
                ('h_mem', models.CharField(max_length=20, blank=True)),
                ('h_disk', models.CharField(max_length=30, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ip_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('h_ip', models.IPAddressField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='host_info',
            name='h_ip',
            field=models.ForeignKey(to='asset.ip_info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cmd_info',
            name='h_ip',
            field=models.ForeignKey(to='asset.ip_info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='app_info',
            name='h_ip',
            field=models.ForeignKey(to='asset.ip_info'),
            preserve_default=True,
        ),
    ]
