from django.contrib import admin

from shorty.models import Url

class UrlAdmin(admin.ModelAdmin):
    list_display = ('long_url', 'short_id', 'counter')
    search_fields = ('long_url', 'short_id')

admin.site.register(Url, UrlAdmin)