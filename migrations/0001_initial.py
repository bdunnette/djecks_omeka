# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'djecks', b'__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Repository',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'url', models.URLField()),
                (b'items_url', models.URLField(blank=True)),
                (b'title', models.CharField(max_length=255, blank=True)),
                (b'repository', models.ForeignKey(to=b'djecks_omeka.Repository', to_field='id')),
                (b'deck', models.ForeignKey(to_field='id', blank=True, to=b'djecks.Deck', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
