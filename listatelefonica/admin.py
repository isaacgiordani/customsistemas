from django.contrib import admin

# Register your models here.
from .models import Entity, PhoneBook

class EntityAdmin(admin.ModelAdmin):
    list_display = ['name','slug','created','modified']
    search_fields = ['name','slug']

class PhoneBookAdmin(admin.ModelAdmin):
    list_display = ['entity','name','lastname','slug','modified']
    search_fields = ['name','slug']

admin.site.register(Entity, EntityAdmin)
admin.site.register(PhoneBook, PhoneBookAdmin)
