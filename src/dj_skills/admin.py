from django.contrib import admin

from .models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "description")
    list_filter = ("user",)
    search_fields = ("name", "description")
