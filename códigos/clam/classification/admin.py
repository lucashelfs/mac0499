from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.tmp_storages import CacheStorage
from .models import Tweet, Review

class TweetResource(resources.ModelResource):

    class Meta:
        model = Tweet
        export_order = ('tweet_id', 'tweet_username', 'tweet_text', 'id')

class TweetAdmin(ImportExportModelAdmin):
    tmp_storage_class = CacheStorage
    resource_class = TweetResource


admin.site.register(Tweet, TweetAdmin)
admin.site.register(Review)
