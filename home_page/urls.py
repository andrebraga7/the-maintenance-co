from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('dashboard', views.Dashboard.as_view(), name='dashboard')
]
