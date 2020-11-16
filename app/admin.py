from django.contrib import admin
from .models import *

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
    ]
    list_filter = ['active', 'category']
    search_fields = ['active', 'category']



admin.site.register(Post,ItemAdmin)
admin.site.register(Category)