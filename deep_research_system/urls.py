# deep_research_system/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('research_app.urls')),  # include app URLs
]
