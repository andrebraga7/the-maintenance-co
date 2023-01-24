from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls'), name='home_page_urls'),
    path('accounts/', include('allauth.urls')),
]
