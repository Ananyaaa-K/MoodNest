from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('habit/', views.get_habit, name='get_habit'),
    path('signup/', views.signup, name='signup'),
    path('auth/', include('django.contrib.auth.urls')),
    path('history/', views.history, name='history'),
    path('profile/', views.profile, name='profile'),
]
