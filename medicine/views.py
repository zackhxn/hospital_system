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
from common.models import medicine

def show(request):
    t = loader.get_template("medicine.html")  # 去模板层找页面

    m = medicine.objects.values()


    html = t.render({'medicine': m})

    return HttpResponse(html)

def submit(request):
    medicine.objects.create(name=request.POST['name'],
                           price=request.POST['price'],
                           number=request.POST['number'],
                           remark=request.POST['remark'],
                           specification=request.POST['specification'],
                            productiondate = request.POST['productiondate'],
                            shelflife = request.POST['shelflife'],
                            )

    return HttpResponseRedirect('/medicine/')