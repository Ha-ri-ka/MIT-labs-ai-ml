from django.urls import path
from . import views


urlpatterns=[
        path('',views.func1,name='func1'),
        path('success',views.func2,name='func2'),
    ]