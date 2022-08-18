from django.urls import path
from user_profile.views import profile_view


urlpatterns = [
    path('profile/<str:profile>/', profile_view, name='profile')
]