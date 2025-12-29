# research_app/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ResearchSession, ResearchReasoning, UploadedDocument, ResearchCost
from .serializers import ResearchSessionSerializer, ResearchReasoningSerializer, UploadedDocumentSerializer, ResearchCostSerializer
from .tasks import execute_research_task

# Home page
def home(request):
    return render(request, 'research_app/home.html')

# Reasoning list view
class ReasoningListView(ListView):
    model = ResearchReasoning
    template_name = 'research_app/reasoning_list.html'
    context_object_name = 'reasonings'

# API: Start Research
class StartResearchAPIView(APIView):
    def post(self, request):
        user = request.user
        query = request.data.get('query')
        parent_id = request.data.get('parent_id', None)
        parent = ResearchSession.objects.filter(id=parent_id).first() if parent_id else None
        session = ResearchSession.objects.create(user=user, query=query, parent=parent)
        execute_research_task.delay(session.id)  # Async execution
        serializer = ResearchSessionSerializer(session)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# API: Continue Research
class ContinueResearchAPIView(APIView):
    def post(self, request, session_id):
        parent = get_object_or_404(ResearchSession, id=session_id)
        query = request.data.get('query')
        session = ResearchSession.objects.create(user=request.user, query=query, parent=parent)
        execute_research_task.delay(session.id)
        serializer = ResearchSessionSerializer(session)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# API: Upload Context File
class UploadDocumentAPIView(APIView):
    def post(self, request, session_id):
        session = get_object_or_404(ResearchSession, id=session_id)
        file = request.FILES['file']
        doc = UploadedDocument.objects.create(session=session, file=file)
        # TODO: Extract text for research
        serializer = UploadedDocumentSerializer(doc)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# API: Get Research History
class ResearchHistoryAPIView(APIView):
    def get(self, request):
        sessions = ResearchSession.objects.filter(user=request.user)
        serializer = ResearchSessionSerializer(sessions, many=True)
        return Response(serializer.data)

# API: Get Research Details
class ResearchDetailAPIView(APIView):
    def get(self, request, session_id):
        session = get_object_or_404(ResearchSession, id=session_id)
        session_serializer = ResearchSessionSerializer(session)
        reasonings_serializer = ResearchReasoningSerializer(session.reasonings.all(), many=True)
        cost_serializer = ResearchCostSerializer(getattr(session, 'researchcost', None))
        return Response({
            'session': session_serializer.data,
            'reasonings': reasonings_serializer.data,
            'cost': cost_serializer.data if cost_serializer else None
        })
from django.http import HttpResponse
from .tasks import execute_research_task

def run_task(request):
    execute_research_task()  # Call your task
    return HttpResponse("Task executed successfully!")
from django.http import HttpResponse
from .tasks import execute_research_task

def home(request):
    return HttpResponse("Welcome to the Deep Research System!")

def run_task(request):
    execute_research_task()
    return HttpResponse("Task executed successfully!")
from django.shortcuts import render
from .tasks import execute_research_task

def home(request):
    return render(request, 'research_app/home.html')

def run_task(request):
    # Execute your research task
    execute_research_task()
    return render(request, 'research_app/task_done.html')
# research_app/views.py

def home(request):
    return render(request, "research/home.html")  # Must match folder name

def reasoning_list(request):
    return render(request, "research/reasoning_list.html")
# research_app/views.py
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, "research/home.html")

def search_results(request):
    query = request.GET.get('query', '')
    
    # Simulate AI research result (replace this with your AI logic)
    result = f"Results for '{query}' will appear here."

    return JsonResponse({'result': result})

from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, "research/home.html")  # Must match folder structure

def search(request):
    topic = request.GET.get('topic', '')
    if topic:
        # Example: return dummy AI result
        result = f"AI result for '{topic}'"
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'result': 'Please enter a topic'})
