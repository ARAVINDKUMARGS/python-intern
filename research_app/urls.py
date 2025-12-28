from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reasonings/', views.research_reasoning_list, name='reasoning-list'),
]
