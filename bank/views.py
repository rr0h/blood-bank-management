from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Donor, BloodInventory, BloodRequest
from .forms import DonorRegistrationForm, BloodRequestForm, UserRegisterForm

def home(request):
    """Home page with blood inventory overview"""
    inventory = BloodInventory.objects.all()
    recent_requests = BloodRequest.objects.filter(status='pending')[:5]
    total_donors = Donor.objects.filter(is_available=True).count()
    
    context = {
        'inventory': inventory,
        'recent_requests': recent_requests,
        'total_donors': total_donors,
    }
    return render(request, 'bank/home.html', context)

def register_donor(request):
    """Donor registration page"""
    if request.method == 'POST':
        form = DonorRegistrationForm(request.POST)
        if form.is_valid():
            donor = form.save(commit=False)
            if request.user.is_authenticated:
                donor.user = request.user
            donor.save()
            
            # Update inventory
            blood_type = donor.blood_type
            inventory, created = BloodInventory.objects.get_or_create(blood_type=blood_type)
            inventory.units_available += 1
            inventory.save()
            
            messages.success(request, 'Donor registered successfully!')
            return redirect('home')
    else:
        form = DonorRegistrationForm()
    
    return render(request, 'bank/register_donor.html', {'form': form})

def donor_list(request):
    """List all donors with search functionality"""
    query = request.GET.get('q', '')
    blood_type = request.GET.get('blood_type', '')
    
    donors = Donor.objects.filter(is_available=True)
    
    if query:
        donors = donors.filter(
            Q(full_name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query)
        )
    
    if blood_type:
        donors = donors.filter(blood_type=blood_type)
    
    context = {
        'donors': donors,
        'query': query,
        'blood_type': blood_type,
    }
    return render(request, 'bank/donor_list.html', context)

def request_blood(request):
    """Blood request form"""
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save(commit=False)
            if request.user.is_authenticated:
                blood_request.requested_by = request.user
            blood_request.save()
            messages.success(request, 'Blood request submitted successfully!')
            return redirect('home')
    else:
        form = BloodRequestForm()
    
    return render(request, 'bank/request_blood.html', {'form': form})

def request_list(request):
    """List all blood requests"""
    requests = BloodRequest.objects.all()
    
    status_filter = request.GET.get('status', '')
    if status_filter:
        requests = requests.filter(status=status_filter)
    
    context = {
        'requests': requests,
        'status_filter': status_filter,
    }
    return render(request, 'bank/request_list.html', context)

def inventory_view(request):
    """Blood inventory page"""
    inventory = BloodInventory.objects.all()
    return render(request, 'bank/inventory.html', {'inventory': inventory})

def register_user(request):
    """User registration"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    
    return render(request, 'bank/register.html', {'form': form})

def login_user(request):
    """User login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'bank/login.html')

def logout_user(request):
    """User logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('home')
