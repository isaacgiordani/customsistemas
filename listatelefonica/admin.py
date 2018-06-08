from django.contrib import admin

# Register your models here.
from .models import Entity, PhoneBook, AccessType, Access

class EntityAdmin(admin.ModelAdmin):
    list_display = ['name','slug','created','modified']
    search_fields = ['name','slug']

class PhoneBookAdmin(admin.ModelAdmin):
    list_display = ['name','lastname','slug','entity','modified']
    search_fields = ['name','slug']

class AccessTypeAdmin(admin.ModelAdmin):
    list_display = ['description','created','modified']
    search_fields = ['description']

class AccessAdmin(admin.ModelAdmin):
    list_display = ['entity','accesstype','identifier','password','description','modified']
    search_fields = ['entity','accesstype','identifier']

admin.site.register(Entity, EntityAdmin)
admin.site.register(PhoneBook, PhoneBookAdmin)
admin.site.register(AccessType, AccessTypeAdmin)
admin.site.register(Access, AccessAdmin)
