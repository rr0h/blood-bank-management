from django.contrib import admin
from .models import Donor, BloodInventory, BloodRequest

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'blood_type', 'phone', 'is_available', 'last_donation_date', 'created_at']
    list_filter = ['blood_type', 'is_available', 'created_at']
    search_fields = ['full_name', 'email', 'phone']
    list_editable = ['is_available']

@admin.register(BloodInventory)
class BloodInventoryAdmin(admin.ModelAdmin):
    list_display = ['blood_type', 'units_available', 'last_updated']
    list_editable = ['units_available']

@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'blood_type', 'units_needed', 'urgency', 'status', 'created_at']
    list_filter = ['blood_type', 'status', 'urgency', 'created_at']
    search_fields = ['patient_name', 'hospital_name', 'contact_number']
    list_editable = ['status']
