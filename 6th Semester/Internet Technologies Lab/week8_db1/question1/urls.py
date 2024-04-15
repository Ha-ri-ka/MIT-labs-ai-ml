from django.urls import path
from . import views

from django.urls import path
from . import views


urlpatterns=[
        path('ex',views.func,name='func'),
        path('reg',views.register,name='register'),
    ]