from django.contrib import admin
from .models import CustomUser, Item, Text, Cart#, Address

admin.site.register(CustomUser)
admin.site.register(Item)
admin.site.register(Text)
admin.site.register(Cart)
#admin.site.register(Address)

class Imageadmin(admin.ModelAdmin):
    list_display = ['title', 'image']