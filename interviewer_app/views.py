from django.shortcuts import render
from django.http import HttpResponse


def interviewer_applicants(request):
    return render(request, 'Applicants.html')

def interviewer_appointments(request):
    return render(request, 'Appointments.html')

def interviewer_editfeedback(request):
    return render(request, 'EditFeedback.html')

def interviewer_feedback(request):
    return render(request, 'Feedback.html')

def interviewer_history(request):
    return render(request, 'History.html')

def interviewer_profile(request):
    return render(request, 'Profile.html')

def interviewer_viewinfo(request):
    return render(request, 'ViewInfo.html')








