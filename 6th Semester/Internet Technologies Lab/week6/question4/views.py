from django.shortcuts import render
from django.http import HttpResponse

def func(request):
    return render(request,'question4/templates/first.html')

def func2(req):
    context={}
    context['total']=0
    if req.method=="POST":
        context['brand']=req.POST['options']
        if 'phones' in req.POST:
            phone_quant=int(req.POST['phone-quantity'],0)
            context['ph_quant']=phone_quant
            if(context['ph_quant']<0): context['ph_quant']=0
            context['phone_cost']=context['ph_quant']*50
            context['total']+=context['phone_cost']
        if 'laptops' in req.POST:
            laptop_quant=int(req.POST['laptop-quantity'],0)
            context['lp_quant']=laptop_quant
            if(context['lp_quant']<0): context['lp_quant']=0
            context['laptop_cost']=context['lp_quant']*100
            context['total']+=context['laptop_cost']
    return render(req,'question4/templates/second.html',context)


