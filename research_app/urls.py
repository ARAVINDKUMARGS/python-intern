# research_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reasonings/', views.ReasoningListView.as_view(), name='reasoning-list'),
    path('api/start/', views.StartResearchAPIView.as_view(), name='start-research'),
    path('api/continue/<int:session_id>/', views.ContinueResearchAPIView.as_view(), name='continue-research'),
    path('api/upload/<int:session_id>/', views.UploadDocumentAPIView.as_view(), name='upload-document'),
    path('api/history/', views.ResearchHistoryAPIView.as_view(), name='research-history'),
    path('api/detail/<int:session_id>/', views.ResearchDetailAPIView.as_view(), name='research-detail'),
]
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('run-task/', views.run_task, name='run_task'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('run-task/', views.run_task, name='run_task'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # Home page
    path('run-task/', views.run_task, name='run_task'),  # Run research task
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('run-task/', views.run_task, name='run_task'),
]

urlpatterns = [
    path('', views.home, name='home'),  # '' means the root URL
]
# research_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('search/', views.search_results, name='search_results'),  # For AJAX/POST search
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('search/', views.search, name='search'),  # Search AJAX
]
