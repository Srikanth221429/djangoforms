from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def Create_school(request):
    ESO=Createschool()
    d={'ESO':ESO}
    if request.method=='POST':
        SO=Createschool(request.POST)
        if SO.is_valid():
            sn=SO.cleaned_data['Sname']
            sp=SO.cleaned_data['Sprinciple']
            sl=SO.cleaned_data['Sbranch']
            e=SO.cleaned_data['Email']
            r=SO.cleaned_data['Reenter']
            DBSO=School.objects.get_or_create(Sname=sn,Sprinciple=sp,Sbranch=sl,email=e,reenteremail=r)[0]
            DBSO.save()
            QLSO=School.objects.all()
            d1={'topic':QLSO}
            return render(request,'display_School.html',d1)
            #return HttpResponse('Data inserted')
        else:
            return HttpResponse('invalid')            
    return render(request,'Create_school.html',d)
