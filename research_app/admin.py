from django.contrib import admin
from .models import ResearchSession, ResearchCost, ResearchReasoning

@admin.register(ResearchSession)
class ResearchSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


@admin.register(ResearchCost)
class ResearchCostAdmin(admin.ModelAdmin):
    list_display = ('id', 'session', 'cost')


@admin.register(ResearchReasoning)
class ResearchReasoningAdmin(admin.ModelAdmin):
    list_display = ('id', 'session', 'reasoning')
