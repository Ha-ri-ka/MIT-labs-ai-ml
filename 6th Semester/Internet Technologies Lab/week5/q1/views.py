from django.shortcuts import render
from django.http import HttpResponse


def studentform(request):
    return render(request,'q1.html')

def showDetails(request):
    context={
        'name':request.GET['name'],
        'dob': request.GET['dob'],
        'mail':request.GET['email'],
        'address':request.GET['addrs'],
        'phone':request.GET['phoneNum'],
        'eng':request.GET['english'],
        'phy':request.GET['physics'],
        'chem':request.GET['chem'],
    }
    return render(request,'q1Output.html',context)
