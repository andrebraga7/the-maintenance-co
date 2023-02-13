from django.urls import path
from . import views

urlpatterns = [
    path('manager/jobs-list', views.JobsList.as_view(), name='jobs_list'),
    path('manager/signup', views.CustomSignupView.as_view(), name='account_signup'),
    path('manager/show-users', views.ShowUsers.as_view(), name='show_users'),
    path('manager/edit_<user_id>', views.EditUser.as_view(), name='edit_user'),
    path('manager/delete_<user_id>', views.DeleteUser.as_view(), name='delete_user'),
    path('manager/jobs/edit_<job_id>', views.EditJob.as_view(), name='edit_job'),
    path('manager/jobs/assign_<job_id>', views.AssignJob.as_view(), name='assign_job'),
    path('manager/jobs/delete_<job_id>', views.ManagerDeleteJob.as_view(), name='delete_job'),
    path('manager/jobs/cancel_delete_<job_id>', views.CancelDeletion.as_view(), name='cancel_delete'),
    path('manager/jobs/done_<job_id>', views.JobDone.as_view(), name='job_done'),
]
