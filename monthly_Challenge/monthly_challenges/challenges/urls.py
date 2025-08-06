# isme list banana hai 
from django.urls import path;
from . import views; 

urlpatterns=[
     # path("january",views.january),
     # path("february",views.february)
     # <int:bla bla> they are knows as path converters
     path("",views.index , name="index"),
     path("<int:month>",views.monthly_challenge_by_number),
     path("<str:month>",views.monthly_challenges,name="month-challenge")
     
     ]