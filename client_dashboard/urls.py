from django.urls import path
from . import views


urlpatterns = [
    path('client/new_jobs', views.NewJobs.as_view(), name='client_new_jobs'),
    path(
        'client/active_jobs',
        views.ActiveJobs.as_view(),
        name='client_active_jobs'),
    path(
        'client/completed_jobs',
        views.CompletedJobs.as_view(),
        name='client_completed_jobs'),
    path('client/categories', views.Categories.as_view(), name='categories'),
    path(
        'client/categories/delete_<category_id>',
        views.DeleteCategory.as_view(), name='delete_category'),
    path(
        'client/categories/edit_<category_id>',
        views.EditCategory.as_view(), name='edit_category'),
    path(
        'client/equipments', views.EquipmentList.as_view(), name='equipments'),
    path(
        'client/add_equipment',
        views.AddEquipment.as_view(), name='add_equipment'),
    path(
        'client/edit_<equipment_id>',
        views.EditEquipment.as_view(), name='edit_equipment'),
    path(
        'client/delete_<equipment_id>',
        views.DeleteEquipment.as_view(), name='delete_equipment'),
    path('client/jobs/add_job', views.AddJob.as_view(), name='add_job'),
    path(
        'client/jobs/edit_<job_id>',
        views.EditJob.as_view(), name='client_edit_job'),
    path(
        'client/jobs/fetch_equipments',
        views.FetchEquipments.as_view(), name='fetch_equipments'),
    path(
        'client/jobs/delete_<job_id>',
        views.DeleteJob.as_view(), name='client_delete_job'),
    path(
        'client/jobs/request_<job_id>',
        views.RequestJobDeletion.as_view(), name='request_job_deletion'),
    path('client/contact', views.Contact.as_view(), name='contact'),
]
