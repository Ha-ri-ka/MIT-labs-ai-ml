from django.urls import path
from . import views


urlpatterns=[
        path('',views.carChoose,name='carChoose'),
        path('carSelected',views.showCar,name='showCar'),
    ]