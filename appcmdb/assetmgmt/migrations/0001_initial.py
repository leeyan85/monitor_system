# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppSoftware',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u5e94\u7528\u8f6f\u4ef6',
                'verbose_name_plural': '\u5e94\u7528\u8f6f\u4ef6',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BcpServers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'BCP\u670d\u52a1\u5668\u5217\u8868',
                'verbose_name_plural': 'BCP\u670d\u52a1\u5668\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u673a\u623f',
                'verbose_name_plural': '\u673a\u623f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DomainName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain_name', models.CharField(max_length=255)),
                ('internal_ipaddr', models.IPAddressField(blank=True)),
                ('bcp_ipaddr', models.IPAddressField(blank=True)),
                ('external_ipaddr', models.IPAddressField(blank=True)),
                ('BCP_server', models.ForeignKey(to='assetmgmt.BcpServers')),
                ('app_software', models.ForeignKey(to='assetmgmt.AppSoftware')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u57df\u540d',
                'verbose_name_plural': '\u57df\u540d',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
                ('desc', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u670d\u52a1\u7ec4',
                'verbose_name_plural': '\u670d\u52a1\u7ec4',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u670d\u52a1\u7ea7\u522b',
                'verbose_name_plural': '\u670d\u52a1\u7ea7\u522b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(unique=True, max_length=255)),
                ('memory', models.CharField(max_length=20)),
                ('cpu', models.CharField(max_length=20)),
                ('bcpserver', models.OneToOneField(null=True, blank=True, to='assetmgmt.BcpServers')),
                ('group', models.ForeignKey(to='assetmgmt.Groups')),
                ('level', models.ForeignKey(to='assetmgmt.ServerLevel')),
                ('location', models.ForeignKey(to='assetmgmt.DataCenter')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u670d\u52a1\u5668\u5217\u8868',
                'verbose_name_plural': '\u670d\u52a1\u5668\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceLines',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u4e1a\u52a1\u7ebf',
                'verbose_name_plural': '\u4e1a\u52a1\u7ebf',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='servers',
            name='serviceline',
            field=models.ForeignKey(to='assetmgmt.ServiceLines'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='domainname',
            name='server',
            field=models.ForeignKey(to='assetmgmt.Servers'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datacenter',
            name='group',
            field=models.ManyToManyField(to='assetmgmt.Groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bcpservers',
            name='location',
            field=models.ForeignKey(to='assetmgmt.DataCenter'),
            preserve_default=True,
        ),
    ]
