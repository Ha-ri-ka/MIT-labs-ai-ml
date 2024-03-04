from django.shortcuts import render
from django.http import HttpResponse

def ques3(request):
    return render(request,'question3/templates/q3.html')