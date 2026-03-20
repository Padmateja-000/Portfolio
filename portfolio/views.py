from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Skill, Project, Certificate, Achievement, Education, Training, ContactMessage

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Please fill out all fields.')

    context = {
        'skills': Skill.objects.all().order_by('-proficiency'),
        'projects': Project.objects.all().order_by('-created_at'),
        'certificates': Certificate.objects.all().order_by('-date_issued'),
        'achievements': Achievement.objects.all().order_by('-date'),
        'educations': Education.objects.all().order_by('-start_date'),
        'trainings': Training.objects.all().order_by('-start_date'),
    }
    return render(request, 'portfolio/index.html', context)
