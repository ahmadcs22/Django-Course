from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('students/', include('students.urls')),
    path('accounts/', include('accounts.urls')),
]

#127.0.0.1/projects/
