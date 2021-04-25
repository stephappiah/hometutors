from django.shortcuts import render
from .models import User

def homestud_email(request):
    all_users = User.objects.all()
    stud_guard = User.objects.filter(is_tutor=False)
    tutors = User.objects.filter(is_tutor=True)
    
    context = {

    }
    return render(request, 'users/homestud_email.html', context)
