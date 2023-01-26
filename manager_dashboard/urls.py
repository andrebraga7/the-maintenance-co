from django.urls import path
from . import views

urlpatterns = [
    path('manager/', views.NewJobs.as_view(), name='manager'),
    path('manage_active/', views.ActiveJobs.as_view(), name='manager_active'),
    path('manage_complete/', views.CompleteJobs.as_view(), name='manager_complete'),

]
