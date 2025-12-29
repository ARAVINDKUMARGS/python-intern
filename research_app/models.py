# research_app/models.py
from django.db import models
from django.contrib.auth.models import User

class ResearchSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.TextField()
    summary = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)  # Important
    updated_at = models.DateTimeField(auto_now=True)

class ResearchReasoning(models.Model):
    session = models.ForeignKey(ResearchSession, on_delete=models.CASCADE)
    reasoning_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ResearchCost(models.Model):
    session = models.ForeignKey(ResearchSession, on_delete=models.CASCADE)
    tokens_used = models.IntegerField(default=0)
    cost = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
# research_app/models.py
from django.db import models
from django.contrib.auth.models import User

class UploadedDocument(models.Model):
    session = models.ForeignKey('ResearchSession', on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.session.id} - {self.document.name}"
