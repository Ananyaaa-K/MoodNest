import random
from datetime import timedelta
from django.utils import timezone
from .models import UserMoodLog

def get_random_quote():
    quotes = [
        "Believe you can and you're halfway there.",
        "Act as if what you do makes a difference. It does.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "You are never too old to set another goal or to dream a new dream.",
        "It always seems impossible until it's done.",
        "Keep your face always toward the sunshine—and shadows will fall behind you.",
        "The only way to do great work is to love what you do.",
        "Small steps in the right direction can turn out to be the biggest step of your life.",
        "Don't watch the clock; do what it does. Keep going.",
        "Happiness is not something ready made. It comes from your own actions."
    ]
    return random.choice(quotes)

def get_user_streak(user):
    if not user.is_authenticated:
        return 0
    
    # Get all distinct dates where the user logged a mood, ordered by latest first
    logs = UserMoodLog.objects.filter(user=user).dates('timestamp', 'day', order='DESC')
    
    if not logs:
        return 0

    streak = 0
    current_date = timezone.now().date()
    
    # Check if the most recent log was today or yesterday
    # If the last log was older than yesterday, the streak is broken (0)
    if logs[0] < current_date - timedelta(days=1):
        return 0

    # Iterate through dates to find consecutive days
    check_date = logs[0] # Start checking from the most recent logged date
    
    for date in logs:
        if date == check_date:
            streak += 1
            check_date -= timedelta(days=1)
        else:
            break
            
    return streak
