from django.shortcuts import render
from .models import ResearchSession, ResearchCost, ResearchReasoning

def home(request):
    sessions = ResearchSession.objects.all()
    return render(request, 'research_app/home.html', {'sessions': sessions})

def session_list(request):
    sessions = ResearchSession.objects.all()
    return render(request, 'research_app/session_list.html', {'sessions': sessions})

def research_cost_list(request):
    costs = ResearchCost.objects.all()
    return render(request, 'research_app/research_cost_list.html', {'costs': costs})

def research_reasoning_list(request):
    reasonings = Reasoning.objects.all()
    return render(request, 'research_app/research_reasoning_list.html', {'reasonings': reasonings})
# research_app/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'research_app/home.html')
from django.shortcuts import render
from .models import Reasoning  # <-- add this

def research_reasoning_list(request):
    reasonings = Reasoning.objects.all()
    return render(request, 'research_app/reasonings.html', {'reasonings': reasonings})
