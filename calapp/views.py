from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,template_name='input.html')
def calculate(request):
    x=int(request.POST["t1"])
    y=int(request.POST["t2"])
    z=request.POST["opt"]
    con_dict={}
    if z=="add":
        con_dict["res"]=x+y
    elif z=="sub":
        con_dict["res"]=x-y
    elif z=="mul":
        con_dict["res"]=x*y
    else:
        con_dict["res"]=x/y
    return render(request,template_name='result.html',context=con_dict)

