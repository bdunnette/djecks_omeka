from django.contrib import admin

# Register your models here.
from djecks_omeka.models import Repository, Collection, Item, Image

class CollectionAdmin(admin.ModelAdmin):
    #readonly_fields = ('url', 'title', 'items_url', 'repository')
    list_filter = ('repository',)

class ItemAdmin(admin.ModelAdmin):
    list_filter = ('collection',)
    
admin.site.register(Repository)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Image)
