from django.urls import path
from . import views

urlpatterns=[
    path('',views.ques2,name='ques2'),
]