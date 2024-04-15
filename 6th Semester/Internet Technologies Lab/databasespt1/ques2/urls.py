from django.urls import path
from . import views

urlpatterns=[
    path('',views.func,name='func'),
    path('q2_pt2',views.find_employee,name='find_employee')
]

