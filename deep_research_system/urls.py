# deep_research_system/urls.py

from django.contrib import admin
from django.urls import path
from research_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('reasonings/', views.reasoning_list, name='reasoning-list'),
]

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('research_app.urls')),  # Include app URLs
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('research_app.urls')),  # Include app URLs
]
