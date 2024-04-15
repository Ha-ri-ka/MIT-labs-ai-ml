from django.shortcuts import render,redirect
from .models import food
# Create your views here.

def index(req):
    if req.method=='POST':
        calories={}
        if req.method=='POST':
            if 'banana' in req.POST:
                calories['banana']=food.objects.get(name='banana').calorie
            if 'apple' in req.POST:
                calories['apple']=food.objects.get(name='apple').calorie
            if 'pizza' in req.POST:
                calories['pizza']=food.objects.get(name='pizza').calorie
            if 'potato' in req.POST:
                calories['potato']=food.objects.get(name='potato').calorie
            # return render(req,)
        print(calories)
        return render(req,'output.html',{'calories':calories})
    return render(req,'input.html')

def func(req):
    calories={}
    if req.method=='POST':
        if 'banana' in req.POST:
            calories['banana']=food.objects.get(name='banana').calorie
        if 'apple' in req.POST:
            calories['apple']=food.objects.get(name='apple').calorie
        if 'pizza' in req.POST:
            calories['pizza']=food.objects.get(name='pizza').calorie
        if 'potato' in req.POST:
            calories['potato']=food.objects.get(name='potato').calorie
        # return render(req,)
    print(calories)
    return render(req,'output.html',calories)


