from django.urls import path
from . import views


urlpatterns = [
    path(
        'client/jobs-list',
        views.ClientJobsList.as_view(), name='client_jobs_list'),
    path('client/categories', views.Categories.as_view(), name='categories'),
    path(
        'client/categories/delete_<category_id>',
        views.DeleteCategory.as_view(), name='delete_category'),
    path(
        'client/categories/edit_<category_id>',
        views.EditCategory.as_view(), name='edit_category'),
]
