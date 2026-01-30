from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import MoodHabit, UserMoodLog
from .utils import get_random_quote, get_user_streak
import random

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def home(request):
    moods = MoodHabit.MOOD_CHOICES
    quote = get_random_quote()
    streak = get_user_streak(request.user)
    return render(request, 'habits/home.html', {
        'moods': moods, 
        'quote': quote,
        'streak': streak
    })

def get_habit(request):
    mood = request.GET.get('mood')
    mood_text = request.GET.get('mood_text')
    exclude_id = request.GET.get('exclude')
    
    # Keyword mapping logic
    if mood_text:
        text = mood_text.lower()
        mapping = {
            'tired': ['tired', 'exhausted', 'sleepy', 'drained', 'burned out'],
            'anxious': ['anxious', 'scared', 'worried', 'nervous', 'fear'],
            'stressed': ['stressed', 'overwhelmed', 'pressure', 'busy'],
            'lazy': ['lazy', 'unmotivated', 'bored', 'unproductive', 'sluggish'],
            'sad': ['sad', 'unhappy', 'lonely', 'depressed', 'crying'],
            'neutral': ['neutral', 'okay', 'fine', 'normal', 'plain']
        }
        
        for category, keywords in mapping.items():
            if any(k in text for k in keywords):
                mood = category
                break
        
        # Fallback to neutral if no keyword found
        if not mood:
            mood = 'neutral'

    habits = MoodHabit.objects.filter(mood=mood, is_active=True)
    
    # Exclude the habit we just saw if shuffling
    if exclude_id:
        habits = habits.exclude(id=exclude_id)
    
    if not habits.exists():
        # If we filtered everything out (e.g. only 1 habit exists), reset filter
        habits = MoodHabit.objects.filter(mood=mood, is_active=True)
        if not habits.exists():
             return render(request, 'habits/result.html', {'error': 'No habits found for this mood.'})
    
    habit = random.choice(list(habits))
    
    # Log mood if user is logged in AND it's not a shuffle (optional, but let's log everything for now)
    if request.user.is_authenticated and not exclude_id:
        UserMoodLog.objects.create(
            user=request.user,
            mood=mood,
            habit_text=habit.habit_text
        )
        
    return render(request, 'habits/result.html', {'habit': habit})

@login_required
def history(request):
    logs = UserMoodLog.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'habits/history.html', {'logs': logs})

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('home')
    return render(request, 'users/profile.html')

@login_required
def history(request):
    logs = UserMoodLog.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'habits/history.html', {'logs': logs})
