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
    path('client/add_job', views.AddJob.as_view(), name='add_job'),
]
