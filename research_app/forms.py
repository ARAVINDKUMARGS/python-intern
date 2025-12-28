from django import forms
from .models import ResearchSession, ResearchCost, ResearchReasoning

class ResearchSessionForm(forms.ModelForm):
    class Meta:
        model = ResearchSession
        fields = ['title', 'description']

class ResearchCostForm(forms.ModelForm):
    class Meta:
        model = ResearchCost
        fields = ['session', 'cost']

class ResearchReasoningForm(forms.ModelForm):
    class Meta:
        model = ResearchReasoning
        fields = ['session', 'content']
