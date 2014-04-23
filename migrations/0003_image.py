# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'djecks_omeka', b'0002_item'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'title', models.CharField(max_length=255, blank=True)),
                (b'description', models.TextField(blank=True)),
                (b'image', models.ImageField(null=True, upload_to=b'omeka/images', blank=True)),
                (b'image_annotated', models.ImageField(null=True, upload_to=b'omeka/images', blank=True)),
                (b'item', models.ForeignKey(to=b'djecks_omeka.Item', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
