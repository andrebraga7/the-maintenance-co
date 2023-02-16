from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('home/about', views.About.as_view(), name='home_about'),
    path('home/contact', views.Contact.as_view(), name='home_contact'),
    path('dashboard', views.Dashboard.as_view(), name='dashboard')
]
