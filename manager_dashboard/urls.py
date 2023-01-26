from django.urls import path
from . import views

urlpatterns = [
    path('manager/', views.NewJobs.as_view(), name='manager'),
    path('manager_active/', views.ActiveJobs.as_view(), name='manager_active'),
    path('manager_completed/', views.CompletedJobs.as_view(), name='manager_completed'),

]
