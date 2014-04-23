# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'cases', b'__first__'),
        (b'djecks_omeka', b'0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'title', models.CharField(max_length=255, blank=True)),
                (b'url', models.URLField()),
                (b'files_url', models.URLField(blank=True)),
                (b'collection', models.ForeignKey(to=b'djecks_omeka.Collection', to_field='id')),
                (b'case', models.ForeignKey(to_field='id', blank=True, to=b'cases.Case', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
