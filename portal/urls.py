from django.contrib import admin
from django.urls import path
from . import views
from .views import tour_json_view

urlpatterns = [
   
    # mut students portal
    path('', views.mut, name="mut"),
    path('registerunits/', views.register_units, name='register_units'),
    

    path("register", views.register, name="register"),
    path("signin", views.signin, name="signin"),
    path("signout",views.signout,name = "signout"),
    
    path("dashboard",views.dashboard,name = 'dashboard'),
    path("mutsignup",views.mutsignup,name = 'mutsignup'),
    path("profile",views.profile,name = 'profile'),
    path('tour.json', tour_json_view, name='tour_json'),
    path('index', views.homepage, name='index'),
    path("unit",views.unit,name = 'unit'),
   
   
    
    

    ]