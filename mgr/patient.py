from django.http import JsonResponse
import json
from common.models import patient

def dispatcher(request):  #请求的路由  根据方法来处理
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST','PUT','DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)


    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_patient':
        return listpatient(request)
    elif action == 'add_patient':
        return addpatient(request)
    elif action == 'modify_patient':
        return modifypatient(request)
    elif action == 'del_patient':
        return deletepatient(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})

def listpatient(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = patient.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})

def addpatient(request):

    info    = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = patient.objects.create(name=info['name'] ,
                            phonenumber=info['phonenumber'] ,
                            address=info['address'])


    return JsonResponse({'ret': 0, 'id':record.id})


def modifypatient(request):
    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作

    patientid = request.params['id']
    newdata = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        patient = patient.objects.get(id=patientid)
    except patient.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{patientid}`的客户不存在'
        }

    if 'name' in newdata:
        patient.name = newdata['name']
    if 'phonenumber' in newdata:
        patient.phonenumber = newdata['phonenumber']
    if 'address' in newdata:
        patient.address = newdata['address']

    # 注意，一定要执行save才能将修改信息保存到数据库
    patient.save()

    return JsonResponse({'ret': 0})

def deletepatient(request):

    patientid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        patient = patient.objects.get(id=patientid)
    except patient.DoesNotExist:
        return  {
                'ret': 1,
                'msg': f'id 为`{patientid}`的客户不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    patient.delete()

    return JsonResponse({'ret': 0})
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def dispatcher(request):
    qs = patient.objects.values()
    t=loader.get_template("manager.html") #去模板层找页面
    html=t.render({'patients': qs,'patient':qs})
    return HttpResponse(html)