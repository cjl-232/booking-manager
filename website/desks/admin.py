from django.contrib import admin

from .models import Booking, Desk

class DeskAdmin(admin.ModelAdmin):
    list_display = ['floor', 'name', 'height_adjustable']
    
class BookingAdmin(admin.ModelAdmin):
    list_display = ['desk_id', 'start_time', 'end_time', 'is_concluded']

admin.site.register(Desk, DeskAdmin)
admin.site.register(Booking, BookingAdmin)