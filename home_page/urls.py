from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('home/about', views.About.as_view(), name='home_about'),
    path('home/contact', views.Contact.as_view(), name='home_contact'),
    path('dashboard', views.Dashboard.as_view(), name='dashboard'),
    path(
        'home/awaiting_approval',
        views.AwaitingApproval.as_view(), name='awaiting_approval'),
    path(
        'home/edit_account', views.EditAccount.as_view(), name='edit_account'),
    path('signup', views.CustomSignupView.as_view(), name='account_signup'),
    
]
