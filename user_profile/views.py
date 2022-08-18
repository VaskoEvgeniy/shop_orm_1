from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def profile_view(request: HttpRequest, profile: str) -> HttpResponse:
    profile_name = {
        'username': profile,
    }
    return render(request, 'Profile.html', profile_name)