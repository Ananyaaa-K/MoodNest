from django.db import models
from django.contrib.auth.models import User

class MoodHabit(models.Model):
    # ... choices ...
    MOOD_CHOICES = [
        ('tired', 'Tired'),
        ('anxious', 'Anxious'),
        ('stressed', 'Stressed'),
        ('lazy', 'Lazy'),
        ('sad', 'Sad'),
        ('neutral', 'Neutral'),
    ]

    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    habit_text = models.CharField(max_length=255)
    estimated_time = models.IntegerField(help_text="Estimated time in minutes (1-5)")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_mood_display()}: {self.habit_text[:30]}..."

class UserMoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=20)
    habit_text = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mood} - {self.timestamp.date()}"
