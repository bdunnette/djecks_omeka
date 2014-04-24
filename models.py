from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models

from djecks.models import Deck, Case, Card
from djecks_anki.models import AnkiDeck

import requests

class Repository(models.Model):
    url = models.URLField()

    def __unicode__(self):
        return self.url

class Collection(models.Model):
    url = models.URLField()
    items_url = models.URLField(blank=True)
    title = models.CharField(max_length=255, blank=True)
    repository = models.ForeignKey(Repository)
    deck = models.ForeignKey(Deck, blank=True, null=True)

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return self.url
      
class Item(models.Model):
    title = models.CharField(max_length=255, blank=True)
    url = models.URLField()
    files_url = models.URLField(blank=True)
    collection = models.ForeignKey(Collection)
    case = models.ForeignKey(Case, blank=True, null=True)
 
    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return self.url
        
class Image(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='omeka/images', blank=True, null=True)
    image_annotated = models.ImageField(upload_to='omeka/images', blank=True, null=True)
    item = models.ForeignKey(Item)
 
    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return self.image.name
          
def get_title(omeka_object):
    if omeka_object['element_texts']:
        title = [t['text'] for t in omeka_object['element_texts'] if t['element_set']['name'] == "Dublin Core"][0].strip()
        return title
    else:
        return None
      
@receiver(post_save, sender=Repository)
def get_repository_collections(instance, **kwargs):
    collection_url = '%s/collections' % instance.url.rstrip('/')
    print collection_url
    collections_json = requests.get(collection_url).json()
    for c in collections_json:
        collection, created = Collection.objects.get_or_create(url=c['url'], repository = instance)
        collection.items_url = c['items']['url']
        collection.title = get_title(c)
        collection.save()
    
@receiver(pre_save, sender=Collection)
def get_collection_deck(instance, **kwargs):
    collection_deck, created = Deck.objects.get_or_create(source=instance.url)
    print collection_deck
    instance.deck = collection_deck

@receiver(post_save, sender=Collection)
def get_collection_items(instance, **kwargs):
    if instance.items_url:
        items_json = requests.get(instance.items_url).json()
        for i in items_json:
            item, created = Item.objects.get_or_create(url=i['url'], collection = instance)
            item.title = get_title(i)
            item.files_url = i['files']['url']
            item.save()

@receiver(pre_save, sender=Item)
def get_item_case(instance, **kwargs):
    item_case, created = Case.objects.get_or_create(source=instance.url)
    if instance.collection:
        item_case.decks.add(instance.collection.deck)
        item_case.save()
    instance.case = item_case
                    
@receiver(post_save, sender=Item)
def get_item_images(instance, **kwargs):
    if instance.files_url:
        files_json = requests.get(instance.files_url).json()
        for f in files_json:
            print f
            card_title = get_title(f)
            print card_title
            card, created = Card.objects.get_or_create(title=card_title)