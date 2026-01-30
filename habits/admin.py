from django.contrib import admin
from .models import MoodHabit

@admin.register(MoodHabit)
class MoodHabitAdmin(admin.ModelAdmin):
    list_display = ('mood', 'habit_text', 'estimated_time', 'is_active')
    list_filter = ('mood', 'is_active')
    search_fields = ('habit_text',)
