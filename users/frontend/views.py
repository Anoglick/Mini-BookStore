from django.shortcuts import render
from django.contrib.auth.models import User

def user_profile(request, user_id):
    user = User.objects.filter(id=user_id).first()
    return render(request, 'user_profile.html', {'user': user})
