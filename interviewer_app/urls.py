from django.urls import path
from . import views

urlpatterns = [
    path('', views.interviewer_appointments, name='INTappointments'),
    path('profile/', views.interviewer_profile, name='INTprofile'),
    path('applicants/', views.interviewer_applicants, name='INTapplicants'),
    path('viewinfo/', views.interviewer_viewinfo, name='INTviewinfo'),
    path('editfeedback/', views.interviewer_editfeedback, name='INTeditfeedback'),
    path('feedback/', views.interviewer_feedback, name='INTfeedback'),
    path('history/', views.interviewer_history, name='INThistory'),
]