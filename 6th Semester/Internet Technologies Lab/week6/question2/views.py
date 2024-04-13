from django.shortcuts import render, redirect

def page1(request):
    return render(request, 'question2/templates/page1.html')

def page2(request):
    name = request.POST['username']
    roll = request.POST['roll']
    subject = request.POST['subject']
    return render(request, 'question2/templates/page2.html', {'name': name, 'roll': roll, 'subject': subject})
