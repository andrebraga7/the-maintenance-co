from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home_page.urls'), name='home_page_urls'),
    path('', include('manager_dashboard.urls'), name='manager_urls'),
    path('', include('client_dashboard.urls'), name='client_urls'),
    path('', include('employee_dashboard.urls'), name='employee_urls'),
]
