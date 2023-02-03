from django.urls import path
from . import views


urlpatterns = [
    path(
        'client/jobs-list',
        views.ClientJobsList.as_view(), name='client_jobs_list'),
]
