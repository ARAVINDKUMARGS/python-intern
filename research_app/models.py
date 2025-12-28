from django.db import models

class ResearchSession(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class ResearchCost(models.Model):
    session = models.ForeignKey(ResearchSession, on_delete=models.CASCADE)
    cost = models.FloatField()

    def __str__(self):
        return f"{self.session.title} - {self.cost}"


class ResearchReasoning(models.Model):
    session = models.ForeignKey(ResearchSession, on_delete=models.CASCADE)
    reasoning = models.TextField()  # renamed from 'content'

    def __str__(self):
        return f"{self.session.title} - Reasoning"
from django.shortcuts import render
from .models import Reasoning  # <-- add this

def research_reasoning_list(request):
    reasonings = Reasoning.objects.all()
    return render(request, 'research_app/reasonings.html', {'reasonings': reasonings})
from django.db import models

class Reasoning(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
