from django.urls import path
from . import views

urlpatterns = [
    path('manager/jobs-list', views.JobsList.as_view(), name='jobs_list'),
    path('manager/signup', views.CustomSignupView.as_view(), name='account_signup'),
    path('manager/show-users', views.ShowUsers.as_view(), name='show_users'),
]
