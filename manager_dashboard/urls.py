from django.urls import path
from . import views

urlpatterns = [
    path('manager/', views.ManagerDashboard.as_view(), name='manager'),
]
