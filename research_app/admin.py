# research_app/admin.py
from django.contrib import admin
from .models import ResearchSession, ResearchReasoning, ResearchCost

@admin.register(ResearchSession)
class ResearchSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at')
    ordering = ('-created_at',)
    list_filter = ('status',)

@admin.register(ResearchReasoning)
class ResearchReasoningAdmin(admin.ModelAdmin):
    list_display = ('id', 'session', 'reasoning_text', 'created_at')
    ordering = ('-created_at',)
    list_filter = ('created_at',)

@admin.register(ResearchCost)
class ResearchCostAdmin(admin.ModelAdmin):
    list_display = ('id', 'session', 'tokens_used', 'cost', 'created_at')
    ordering = ('-created_at',)
    list_filter = ('created_at',)
