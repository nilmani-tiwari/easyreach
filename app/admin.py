from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(UserContactMessage)
class UserContactMessageAdmin(admin.ModelAdmin):
    list_display = ['user','name','email','subject','active']
    search_fields  = ['user','name','email','subject','created_at']
    list_filter = ['active','created_at']


admin.site.register(Product)