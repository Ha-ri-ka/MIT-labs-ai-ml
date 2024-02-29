from django.urls import path
from . import views

urlpatterns=[
    path('',views.studentform,name='studentform'),
    path('q1Output',views.showDetails,name="showDetails")
]
