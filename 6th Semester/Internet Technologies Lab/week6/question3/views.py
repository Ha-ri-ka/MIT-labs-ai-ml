from django.shortcuts import render
from django.http import HttpResponse


def func1(request):
    return render(request,'question3/templates/register.html')

def func2(request):
    context={}
    if request.method=='POST':
        context['username']=request.POST['username']
        context['password']=request.POST['password']
        context['email']=request.POST['email']
        context['phone']=request.POST['phone']
        return render(request,'question3/templates/success.html',context)
    else:
        return render(request,'question3/templates/register.html')
