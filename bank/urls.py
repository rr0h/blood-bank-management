from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register-donor/', views.register_donor, name='register_donor'),
    path('donors/', views.donor_list, name='donor_list'),
    path('request-blood/', views.request_blood, name='request_blood'),
    path('requests/', views.request_list, name='request_list'),
    path('inventory/', views.inventory_view, name='inventory'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
