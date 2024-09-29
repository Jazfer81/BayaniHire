from django.urls import path
from . import views

urlpatterns = [
    path('', views.applicant_homepage, name='homepage'),
    path('jobreq/<str:job_type>/', views.applicant_jobreq, name='jobreq'),
    path('profile/', views.applicant_profile, name='profile'),
    path('applicationstatus/', views.applicant_applicationstatus, name='applicationstatus'),
    path('jobreq/', views.applicant_jobreq, name='jobreq'),
    path('fileupload/', views.applicant_fileupload, name='fileupload'),
    path('viewfileupload/', views.applicant_viewfileupload, name='viewfileupload'),
    path('interviewdetails/', views.applicant_interviewdetails, name='interviewdetails'),
]
