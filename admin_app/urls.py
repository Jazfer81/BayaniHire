from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_of_applicants, name='list_of_applicants'),
    path('open_applicants/', views.open_applicants, name='open_applicants'),
    path('viewing_files/', views.viewing_files, name='viewing_files'),
    path('list_of_jobs/', views.list_of_jobs, name='list_of_jobs'),
    path('edit_job_details/', views.edit_job_details, name='edit_job_details'),
    path('qualification/', views.qualification, name='qualification'),
    path('send_schedule/', views.send_schedule, name='send_schedule'),
    path('open_schedule_list/', views.open_schedule_list, name='open_schedule_list'),
    path('schedule/', views.schedule, name='schedule'),
    path('feedback/', views.feedback, name='feedback'),
    path('view_feedback/', views.view_feedback, name='view_feedback'),
    path('profile/', views.adminprofile, name='adminprofile'),
    path('add_accounts/', views.add_accounts, name='add_accounts'),
]
