from django.contrib import admin
from django.contrib import admin, messages
from django.db.models import Count, Sum

from notification.models import *

# Register your models here.


def send_now(modeladmin, request, queryset):

    message = ""
    for campaign in queryset:
        message_append = campaign.send_now()
        message += f"{campaign} [{message_append}]"
    messages.success(request, message)
    return
send_now.short_description = "Send right now"



def one_email_send(modeladmin, request, queryset):
    for c in queryset:
        c.send()
    return

@admin.register(EmailOutreach)
class OneOffEmailOutreachAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'from_email', 'created_at', 'modified_at']
    list_filter = ['from_email']
    search_fields = ['name', 'subject','from_email']




@admin.register(UserVerificationCodes)
class UserVerificationCodesAdmin(admin.ModelAdmin):
    list_display = ['id', 'usr', 'otp','verified']
    list_filter = ('usr','verified','created_at')
    search_fields=('usr','verified')
    autocomplete_fields = ['usr',]
