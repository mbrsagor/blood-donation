from django.contrib import admin

from blood.models.location import Location
from blood.models.donor import Donor


class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent', 'is_active']
    search_fields = ['name', 'parent']

admin.site.register(Location, LocationAdmin)


class DonorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'phone_number', 'select_blood', 'last_donation_date', 'gender']
    search_fields = ['first_name', 'phone_number', 'select_blood', 'last_donation_date']
    edit_fields = ['phone_number', 'select_blood']
    link_display = ['id', 'first_name']
    
admin.site.register(Donor, DonorAdmin)