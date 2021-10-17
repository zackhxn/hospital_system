from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from common.models import patient
from common.models import doctor
from common.models import medicalrecord
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from common.models import queue


def showpatient(request,id):  # request HTTP请求信息
    p = patient.objects.get(id=id)
    return render(request, 'patient_main.html', locals())


def register(request,id):  #挂号

    #

    p = patient.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'patient_register.html', locals())

    elif request.method == 'POST':
        q=queue.objects.get(depart=request.POST['department'])
        print(q.queue)
        medicalrecord.objects.create(patient_id=id,
                                     department=request.POST['department'],
                                     queue=q.queue,
                                     doctor_id='0',
                                    now_queue=q.now_queue,
                                     medicinelist_id=0,
                                     )
        q.queue=q.queue+1
        q.save()

        return HttpResponseRedirect('/patient/record/' + str(id))





def update(request,id):
    p = patient.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'patient_update.html', locals())

    elif request.method == 'POST':
        # 改 存
        gender = request.POST['gender']
        old = request.POST['old']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        password = request.POST['password']

        p.gender = gender
        p.old = old
        p.phonenumber = phonenumber
        p.address = address
        p.password =password
        p.save()
        return HttpResponseRedirect('/patient/'+str(id)+'/')

def record(request,id):
    p = medicalrecord.objects.get(patient_id=id)
    return render(request, 'medicalrecord.html', locals())
