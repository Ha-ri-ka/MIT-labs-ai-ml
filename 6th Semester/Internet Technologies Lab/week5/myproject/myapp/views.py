from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name='amma'
    context={
        'name': 'Harika',
        'age': 20,
        'nationality': 'indian'
    }
    return render(request,'myapp/templates/index.html',context)

def counter(request):
    text=request.GET['text']
    numOfWords=len(text.split())
    return render(request,'myapp/templates/counter.html',{'numOfWords':numOfWords})