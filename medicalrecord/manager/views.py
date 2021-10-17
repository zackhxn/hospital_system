from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from common.models import patient
from common.models import doctor
from django.template import loader

def show(request):
    t=loader.get_template("manager.html") #去模板层找页面

    qs = patient.objects.values()
    do = doctor.objects.values()

    html=t.render({'patients': qs,'doctors':do})


    return HttpResponse(html)

def submitpatient(request):
    patient.objects.create(name=request.POST['name'],
                           gender=request.POST['gender'],
                           old=request.POST['old'],
                           phonenumber=request.POST['phonenumber'],
                           address=request.POST['address'])

    return HttpResponseRedirect('/manager/')

def submitdoctor(request):
    doctor.objects.create(name=request.POST['name'],
                           gender=request.POST['gender'],
                           old=request.POST['old'],
                           phonenumber=request.POST['phonenumber'],
                           department=request.POST['department'],
                            outpatient_id=request.POST['outpatient_id'])

    return HttpResponseRedirect('/manager/')

def updatepatient(request,id):
    p = patient.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'manager_updatepatient.html', locals())

    elif request.method == 'POST':
        #改 存
        gender = request.POST['gender']
        old = request.POST['old']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']

        p.gender = gender
        p.old = old
        p.phonenumber = phonenumber
        p.address = address
        p.save()
        return HttpResponseRedirect('/manager/')


def updatedoctor(request,id):
    d = doctor.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'manager_updatedoctor.html', locals())

    elif request.method == 'POST':
        #改 存
        gender = request.POST['gender']
        old = request.POST['old']
        department = request.POST['department']
        phonenumber = request.POST['phonenumber']
        outpatient_id = request.POST['outpatient_id']



        d.gender = gender
        d.old = old
        d.department = department
        d.phonenumber = phonenumber
        d.outpatient_id = outpatient_id

        d.save()
        return HttpResponseRedirect('/manager/')

def deletepatient(request,id):
    p = patient.objects.get(id=id)
    p.delete()
    return HttpResponseRedirect('/manager/')

def deletedoctor(request,id):
    d = doctor.objects.get(id=id)
    d.delete()
    return HttpResponseRedirect('/manager/')


