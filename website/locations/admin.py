from django.contrib import admin

from .models import Floor, Site

class FloorAdmin(admin.ModelAdmin):
    list_display = ['name', 'plan']

admin.site.register(Floor, FloorAdmin)
admin.site.register(Site)
