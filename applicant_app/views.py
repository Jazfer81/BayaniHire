from django.shortcuts import render
from django.http import HttpResponse
from . import views

def applicant_homepage(request):
    return render(request, 'Applicant_homepage.html')

def applicant_profile(request):
    return render(request, 'Applicant_profile.html')

def applicant_applicationstatus(request):
    return render(request, 'Applicant_Applicationstatus.html')

def applicant_jobreq(request, job_type):
    job_details = {}
    if job_type == "doctor":
        job_details = {
            "title": "Doctor",
            "date_published": "01/01/2024",
            "description": "A doctor diagnoses and treats illnesses and injuries in patients. They conduct physical exams, order and interpret diagnostic tests, and develop treatment plans. Doctors also provide preventive care and educate patients about health and wellness.",
            "requirements": "Medical degree, relevant certifications, at least 3 years of experience in a medical field.",
            "benefits": "Healthcare coverage, pension, 30 days vacation, paid time off, professional development programs."
        }
    elif job_type == "teacher":
        job_details = {
            "title": "Teacher",
            "date_published": "01/02/2024",
            "description": "A teacher imparts knowledge and skills to students, fosters a supportive learning environment, and develops lesson plans to aid student progress.",
            "requirements": "Teaching degree, state certifications, experience in lesson planning and classroom management.",
            "benefits": "Pension, summer vacation, 20 days paid time off, professional development courses."
        }
    elif job_type == "helper":
        job_details = {
            "title": "Helper",
            "date_published": "01/03/2024",
            "description": "A helper provides assistance with daily tasks, helping to ensure smooth operations in non-medical environments.",
            "requirements": "Basic experience in assisting roles, strong organizational skills, ability to multitask.",
            "benefits": "Flexible hours, healthcare coverage, 15 days paid vacation."
        }

    return render(request, 'Applicant_JobReq.html', {'job_details': job_details})

def applicant_fileupload(request):
    return render(request, 'Applicant_fileupload.html')

def applicant_viewfileupload(request):
    return render(request, 'Applicant_Viewfileupload.html')

def applicant_interviewdetails(request):
    return render(request, 'Applicant_InterviewDetails.html')








