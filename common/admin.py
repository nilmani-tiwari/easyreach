from django.contrib import admin
from django.utils.html import format_html
from common.models import *

# Register your models here.

@admin.register(SponsorAd)
class SponsorAdsAdmin(admin.ModelAdmin):
    list_display = ['id', 'ads_url', 'file', 'ref_slug','visibility','custom_field']
    search_fields = ['ads_url', 'file', 'ref_slug']

    def custom_field(self, obj):
        return format_html(f'<a href="/show_ads/{obj.pk}">URL</a>')
    
