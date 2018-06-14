from django.contrib import admin

# Register your models here.
from .models import Entity, PhoneBook, AccessType, Access

class EntityAdmin(admin.ModelAdmin):
    list_display = ['name','slug','created','modified']
    search_fields = ['name','slug']
    list_filter = ['created', 'modified']

class PhoneBookAdmin(admin.ModelAdmin):
    list_display = ['name','lastname','slug','entity','modified']
    search_fields = ['name','slug','entity__name']
    list_filter = ['created', 'modified']

class AccessTypeAdmin(admin.ModelAdmin):
    list_display = ['description','created','modified']
    search_fields = ['description']
    list_filter = ['created', 'modified']

class AccessAdmin(admin.ModelAdmin):
    list_display = ['entity','accesstype','identifier','password','description','modified']
    search_fields = ['entity__name','accesstype__description','identifier']
    list_filter = ['created', 'modified']

admin.site.register(Entity, EntityAdmin)
admin.site.register(PhoneBook, PhoneBookAdmin)
admin.site.register(AccessType, AccessTypeAdmin)
admin.site.register(Access, AccessAdmin)
