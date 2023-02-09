from django.urls import path
from . import views

urlpatterns = [
    path('manager/jobs-list', views.JobsList.as_view(), name='jobs_list'),
    path('manager/signup', views.CustomSignupView.as_view(), name='account_signup'),
    path('manager/show-users', views.ShowUsers.as_view(), name='show_users'),
    path('manager/edit_<user_id>', views.EditUser.as_view(), name='edit_user'),
    path('manager/delete_<user_id>', views.DeleteUser.as_view(), name='delete_user'),
    path('manager/<job_id>', views.AssignJob.as_view(), name='assign_job'),
]
