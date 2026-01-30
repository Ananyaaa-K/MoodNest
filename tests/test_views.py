import pytest
from django.urls import reverse
from habits.models import MoodHabit

@pytest.mark.django_db
def test_home_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert 'MoodNest' in str(response.content)

@pytest.mark.django_db
def test_get_habit_view(client):
    MoodHabit.objects.create(mood='tired', habit_text='Sleep', estimated_time=5, is_active=True)
    url = reverse('get_habit')
    response = client.get(url, {'mood': 'tired'})
    assert response.status_code == 200
    assert 'Sleep' in str(response.content)

@pytest.mark.django_db
def test_get_habit_no_results(client):
    url = reverse('get_habit')
    response = client.get(url, {'mood': 'unknown'})
    assert response.status_code == 200
    assert 'No habits found' in response.content.decode()
