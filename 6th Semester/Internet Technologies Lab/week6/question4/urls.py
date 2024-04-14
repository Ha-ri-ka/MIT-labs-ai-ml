from django.urls import path
from . import views


urlpatterns=[
        path('',views.func,name='func'),
        path('second',views.func2,name='func2'),
    ]