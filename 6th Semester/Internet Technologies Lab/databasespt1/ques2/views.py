from django.shortcuts import render,redirect
from .models import works,lives

def func(req):
    if req.method=='POST':
        name=req.POST['name']
        comp_name=req.POST['comp_name']
        salary=req.POST['salary']
        street=req.POST['street']
        city=req.POST['city']

        workObject=works.objects.create(person_name=name,company_name=comp_name,salary=salary)
        workObject.save()

        livesObject=lives.objects.create(person_name=name,street=street,city=city)
        livesObject.save()
        return redirect('/ques2')
    else:
        return render(req,'ques2/templates/q2.html')
    
def find_employee(req):
    if req.method=='POST':
        comp=req.POST['key']
        emplist=[]
        employees=works.objects.filter(company_name=comp)
        for emp in employees:
            emplist.append(emp.person_name)
        cities=[]
        for emp in employees:
            city=lives.objects.filter(person_name=emp.person_name)
            if city.exists():
                    cities.extend(city.values_list('city', flat=True))
            print(cities)  
            return render(req, 'ques2/templates/q2_pt2.html', {'employees': emplist, 'cities': cities,'company':comp})
        else:
            return redirect('/ques2')
    else:
        return redirect('/ques2')
            


# Create your views here.
