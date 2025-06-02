from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),             # http://localhost:8000/
    path('about/', views.about, name='about'),     # http://localhost:8000/about/
    path('contact/', views.contact, name='contact')# http://localhost:8000/contact/
]