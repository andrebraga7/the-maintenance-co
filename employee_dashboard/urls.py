from django.urls import path
from . import views

urlpatterns = [
    path(
        'employee/active-jobs',
        views.EmployeeActiveJobs.as_view(),
        name='employee_active_jobs'),
    path(
        'employee/completed-jobs',
        views.EmployeeCompletedJobs.as_view(),
        name='employee_completed_jobs'),
    path(
        'employee/add-feedback/<job_id>',
        views.AddFeedback.as_view(),
        name='add_feedback'),
    path(
        'employee/mark-as-done/<job_id>',
        views.JobDone.as_view(),
        name='mark-as-done'),
]
