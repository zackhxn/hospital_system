from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from common.models import patient

from django.template import loader
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from common.models import patient
from common.models import doctor
from common.models import manager
from common.models import medicinemanager
from django.contrib import messages

def mainpage(request):
    return render(request, "login.html")

def log_in_patient(request):
    id = request.POST['id']
    password = request.POST['password']
    s = patient.objects.get(id=id)
    if request.method == 'POST':
        if s.password==password:
            return HttpResponseRedirect('/patient/'+id+'/')
        else:
            messages.success(request, "登录失败！")
            return HttpResponseRedirect('/login/')


def log_in_manager(request):
    id = request.POST['id']
    password = request.POST['password']
    s = patient.objects.get(id=id)
    if request.method == 'POST':
        if s.password==password:
            return HttpResponseRedirect('/manager/')
        else:
            messages.success(request, "登录失败！")
            return HttpResponseRedirect('/login/')

def log_in_doctor(request):
    id = request.POST['id']
    password = request.POST['password']
    s = patient.objects.get(id=id)
    if request.method == 'POST':
        if s.password==password:
            return HttpResponseRedirect('/doctor/'+id+'/')
        else:
            messages.success(request, "登录失败！")
            return HttpResponseRedirect('/login/')

def log_in_medicinemanager(request):
    id = request.POST['id']
    password = request.POST['password']
    s = patient.objects.get(id=id)
    if request.method == 'POST':
        if s.password==password:
            return HttpResponseRedirect('/medicine/')
        else:
            messages.success(request, "登录失败！")
            return HttpResponseRedirect('/login/')
            # return HttpResponse('登录失败')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':

        patient.objects.create(name=request.POST['name'],
                               gender=request.POST['gender'],
                               old=request.POST['old'],
                               phonenumber=request.POST['phonenumber'],
                               address=request.POST['address'],
                               password=request.POST['password'],)
        p=patient.objects.get(phonenumber=request.POST['phonenumber'])

        return HttpResponseRedirect('/patient/' + str(p.id)+'/')
