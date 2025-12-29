# research_app/serializers.py
from rest_framework import serializers
from .models import ResearchSession, ResearchReasoning, UploadedDocument, ResearchCost

class ResearchSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchSession
        fields = '__all__'

class ResearchReasoningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchReasoning
        fields = '__all__'

class UploadedDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedDocument
        fields = '__all__'

class ResearchCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchCost
        fields = '__all__'
