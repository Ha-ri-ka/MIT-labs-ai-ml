from django.shortcuts import render
from django.http import HttpResponse

def ques2(request):
    return render(request,'question2/templates/q2.html')