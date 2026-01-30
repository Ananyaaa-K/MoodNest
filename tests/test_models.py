import pytest
from habits.models import MoodHabit, UserMoodLog
from django.contrib.auth.models import User
from django.utils import timezone

@pytest.mark.django_db
def test_create_mood_habit():
    habit = MoodHabit.objects.create(
        mood='tired',
        habit_text='Take a nap',
        estimated_time=20
    )
    assert habit.mood == 'tired'
    assert habit.habit_text == 'Take a nap'
    assert str(habit) == 'Tired: Take a nap...'

@pytest.mark.django_db
def test_user_mood_log():
    user = User.objects.create(username='testuser')
    log = UserMoodLog.objects.create(
        user=user,
        mood='happy',
        habit_text='Dance'
    )
    assert log.user.username == 'testuser'
    assert log.timestamp <= timezone.now()
