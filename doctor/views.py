from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from  common.models import  patient
#
# def listorders(request):  #处理请求
#     return HttpResponse("下面是系统中所有的订单信息。。。")
#
#
# # 先定义好HTML模板
# html_template = '''
#
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="UTF-8">
# <style>
# table {
#     border-collapse: collapse;
# }
# th, td {
#     padding: 8px;
#     text-align: left;
#     border-bottom: 1px solid #ddd;
# }
# </style>
# </head>
#     <body>
#         <table>
#         <tr>
#         <th>id</th>
#         <th>姓名</th>
#         <th>电话号码</th>
#         <th>地址</th>
#         </tr>
#
#          {% for patient in patients %}
#             <tr>
#
#             {% for name, value in patient.items %}
#                 <td>{{ value }}</td>
#             {% endfor %}
#
#             </tr>
#         {% endfor %}
#
#
#         </table>
#     </body>
# </html>
# '''
# from django.template import engines
# django_engine = engines['django']
# template = django_engine.from_string(html_template)
from common.models import doctor
from django.template import loader
from django.shortcuts import render
from common.models import medicalrecord
from common.models import queue
from common.models import medicine
from common.models import medicinelist
#
#
# def listpatient(request): #request HTTP请求信息
#     # 返回一个 QuerySet 对象 ，包含所有的表记录
#     # 每条表记录都是是一个dict对象，
#     # key 是字段名，value 是 字段值
#     qs = patient.objects.values()
#
#     rendered = template.render({'patients': qs})
#
#     return HttpResponse(rendered)
#
# def test1(request):
#     qs = patient.objects.values()
#     t=loader.get_template("test1.html") #去模板层找页面
#     html=t.render({'patients': qs,'patient':qs})
#     return HttpResponse(html)
#
# def test2(request):
#     #qs = patient.objects.values()
#     qs = [{'id': 1, 'name': '黄西宁', 'phonenumber': '13851917864', 'address': '澄江街道'}, {'id': 2, 'name': '张阿文', 'phonenumber': '13593419666'
#      , 'address': '中山站'}]
#
#     return render(request,"test2.html",{'patients':qs})
from django.http import HttpResponseRedirect

def showdoctor(request,id):  # request HTTP请求信息
    p = doctor.objects.get(id=id)
    return render(request, 'doctor_main.html', locals())

def prescribe(request):

    return render(request, "doctor_prscribe.html")


def update(request,id):
    p = doctor.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'doctor_update.html', locals())

    elif request.method == 'POST':
        # 改 存
        gender = request.POST['gender']
        old = request.POST['old']
        department = request.POST['department']
        phonenumber = request.POST['phonenumber']
        outpatient_id = request.POST['outpatient_id']

        password = request.POST['password']

        p.gender = gender
        p.old = old
        p.department = department
        p.phonenumber = phonenumber
        p.outpatient_id = outpatient_id
        p.password =password
        p.save()
        return HttpResponseRedirect('/doctor/'+str(id)+'/')

def select(request,id):    #医生的id
    d = doctor.objects.get(id=id)
    de = d.department    #医生的department
    m = medicalrecord.objects.values()
    m = m.filter(department=de)
    print(m)
    #找now_queue
    q = queue.objects.get(depart=de)
    print("这是queue",q)

    t = loader.get_template("doctor_select.html")  # 去模板层找页面
    html = t.render({'patients': m,'doctor_id':id,'now_queue':q.now_queue})
    return HttpResponse(html)

def selectpatient(request,id,doctor_id):  #传的id是就诊单id 和医生id   修改对应病人的就诊单
    print("就诊单id",id,"是这个")
    m = medicalrecord.objects.get(id=id)
    m.doctor_id = doctor_id
    m.save()
    q = queue.objects.get(depart=m.department)
    q.now_queue=q.now_queue+1
    q.save()


    me = medicine.objects.values()
    t = loader.get_template("doctor_prescribe.html")  # 去模板层找页面
    html = t.render({'medicine': me,'medicalrecord':id})
    return HttpResponse(html)

def generatelist(request,id):  #id是就诊单     此函数用于生成药品单
    list = medicalrecord.objects.get(id=id)
    if request.method == 'POST':

        for i in request.POST.getlist('medicine_id'):  #i 选择的药品编号
            m = medicine.objects.get(id=i)
            medicinelist.objects.create(medicalrecord_id=id,
                                  patient_id=list.patient_id,
                                  name=m.name,
                                  price=m.price,
                                  number=1,
                                  medicinelist_id=id)
        return HttpResponse('ceshi')





