from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

def check(request):
    SO=StudentForm()
    d={'SO':SO}
    if request.method=='POST':
        SRD=StudentForm(request.POST)
        if SRD.is_valid():
            return HttpResponse('Valid data')
        else:
            return HttpResponse('Not Valid Data')
    return render(request,'validation.html',d)
