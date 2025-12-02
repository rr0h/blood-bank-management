from django.db import models
from django.contrib.auth.models import User

BLOOD_TYPES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    age = models.IntegerField()
    address = models.TextField()
    last_donation_date = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.blood_type}"
    
    class Meta:
        ordering = ['-created_at']

class BloodInventory(models.Model):
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES, unique=True)
    units_available = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.blood_type} - {self.units_available} units"
    
    class Meta:
        verbose_name_plural = "Blood Inventories"
        ordering = ['blood_type']

class BloodRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('fulfilled', 'Fulfilled'),
    ]
    
    patient_name = models.CharField(max_length=200)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    units_needed = models.IntegerField()
    hospital_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)
    reason = models.TextField()
    urgency = models.CharField(max_length=20, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient_name} - {self.blood_type} ({self.units_needed} units)"
    
    class Meta:
        ordering = ['-created_at']
