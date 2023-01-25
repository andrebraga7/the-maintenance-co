from django.urls import path
from . import views

urlpatterns = [
    path('manager/', views.Initial.as_view(), name='manager'),
]
