from django.shortcuts import render
from django.http import HttpResponse


def carChoose(request):
    return render(request,'question1/templates/carOptions.html')

def showCar(request):
    context={
        'manufacturer':request.GET['manufacturer'],
        'model': request.GET['model']
    }
    return render(request,'question1/templates/carSelected.html',context)

