from django.urls import path
from Jobportal import views

urlpatterns=[
    path('',views.home,name="home"),
    path('job_detail/<int:id>/<str:slug_url>',views.job_detail,name="job_detail"),
    path('subscribe/', views.subscribe, name='subscribe' ),
    path('add_jobpost/',views.addjobpost, name = 'add_jobpost'),
    path('recruiter_registration/',views.author,name='recruiter_registration'),
    path('thankyou/', views.thankyou, name='thankyou'),

]