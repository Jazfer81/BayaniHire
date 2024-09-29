from django.shortcuts import render
from django.http import HttpResponse
from . import views

def list_of_applicants(request):
    return render(request, 'AdminView_1_Homepage_ListofApplicants.html')

def open_applicants(request):
    return render(request, 'AdminView_1_1_OpenApplicants.html')

def viewing_files(request):
    return render(request, 'AdminView_1_2_ViewingFiles.html')

def list_of_jobs(request):
    return render(request, 'AdminView_2_ListofJobs.html')

def edit_job_details(request):
    return render(request, 'AdminView_2_1_EditJobDetails.html')

def qualification(request):
    return render(request, 'AdminView_3_Qualification.html')

def send_schedule(request):
    return render(request, 'AdminView_3_1_Send.html')

def open_schedule_list(request):
    return render(request, 'AdminView_3_2_OpenScheduleList.html')

def schedule(request):
    return render(request, 'AdminView_4_Schedule.html')

def feedback(request):
    return render(request, 'AdminView_5_Feedback.html')

def view_feedback(request):
    return render(request, 'AdminView_5_1_ViewFeedback.html')

def adminprofile(request):
    return render(request, 'AdminView_6_Profile.html')

def add_accounts(request):
    return render(request, 'AdminView_6_2_AddAccounts.html')