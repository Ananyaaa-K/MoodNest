from django.core.management.base import BaseCommand
from habits.models import MoodHabit

class Command(BaseCommand):
    help = 'Seed initial habits'

    def handle(self, *args, **kwargs):
        habits_data = [
            ('tired', 'Drink a glass of water', 1),
            ('tired', 'Take a 5-minute power nap', 5),
            ('anxious', 'Take 5 slow, deep breaths', 1),
            ('anxious', 'Write down one thing you are grateful for', 2),
            ('stressed', 'Stretch your arms and neck for 2 minutes', 2),
            ('stressed', 'Step outside for 3 minutes of fresh air', 3),
            ('lazy', 'Stand up and shake your body for 30 seconds', 1),
            ('lazy', 'Wash your face with cold water', 2),
            ('sad', 'Listen to your favorite upbeat song', 4),
            ('sad', 'Wrap yourself in a warm blanket for 5 minutes', 5),
            ('neutral', 'Read one page of a book', 3),
            ('neutral', 'Plan one small task for tomorrow', 2),
        ]

        for mood, text, time in habits_data:
            MoodHabit.objects.get_or_create(
                mood=mood,
                habit_text=text,
                estimated_time=time
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded habits'))
