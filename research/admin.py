from django.contrib import admin
from .models import ResearchSession, ResearchCost, ResearchReasoning


@admin.register(ResearchSession)
class ResearchSessionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)
    ordering = ("-created_at",)


@admin.register(ResearchCost)
class ResearchCostAdmin(admin.ModelAdmin):
    list_display = ("id", "session", "amount", "created_at")
    list_filter = ("created_at",)
    ordering = ("-created_at",)


@admin.register(ResearchReasoning)
class ResearchReasoningAdmin(admin.ModelAdmin):
    list_display = ("id", "session", "reasoning_text", "created_at")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
