from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Feature

def func(request):  
    # feature1=Feature()
    # feature1.id=13
    # feature1.name='harika'
    # feature1.details='we good'
    # feature1.is_true=True

    # feature2=Feature()
    # feature2.id=14
    # feature2.name='harika+1'
    # feature2.details='we good+1'
    # feature2.is_true=False

    # features=[feature1,feature2]
    #U CAN LITERALLY REMOVE EM CAUSE U SET UP DB!!
    features=Feature.objects.all
    return render(request,'question1/templates/index.html',{'features':features})

def register(req):
    username=req.POST['username']
    email=req.POST['email']
    password=req.POST['password']
    if len(password)<3:
        if User.object.filter(email=email).exists():
            messages.info(req,'why are u using same email again? ')
    return render(req,'question1/templates/register.html')