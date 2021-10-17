from django.db import models

# Create your models here.

class patient(models.Model):
    # 病人名称
    name = models.CharField(max_length=200)
    #病人性别
    gender = models.CharField(max_length=20,null=True,blank=True)
    #病人年龄
    old = models.CharField(max_length=20,null=True,blank=True)
    #ID
    # 联系电话
    phonenumber = models.CharField(max_length=200)
    # 地址
    address = models.CharField(max_length=200)

    password = models.CharField(max_length=200,default="123456")

class doctor(models.Model):
    # 医生名称
    name = models.CharField(max_length=200)
    #医生性别
    gender = models.CharField(max_length=20)
    #医生年龄
    old = models.CharField(max_length=20)
    #ID
    # 联系电话
    department = models.CharField(max_length=200)


    #科室
    phonenumber = models.CharField(max_length=200)

    #门诊号
    outpatient_id = models.CharField(max_length=200)
    iswork = models.BigIntegerField(default=0)   #0不在工作 1在工作


    password = models.CharField(max_length=200,default="123456")

class medicine(models.Model):
    #药品库
    name = models.CharField(max_length=200)
    price=models.BigIntegerField()
    number = models.BigIntegerField()
    specification = models.CharField(max_length=200,blank=True)
    remark = models.CharField(max_length=200,blank=True)
    productiondate = models.CharField(max_length=200,blank=True)
    shelflife = models.CharField(max_length=200,blank=True)



class manager(models.Model):
    #管理员表

    password = models.CharField(max_length=200)

class medicinemanager(models.Model):
    #管理员表

    password = models.CharField(max_length=200)

class medicalrecord(models.Model):  #就诊表
    patient_id = models.BigIntegerField()
    doctor_id = models.BigIntegerField(blank=True)
    department = models.CharField(max_length=200)
    medicinelist_id = models.BigIntegerField(blank=True)
    queue = models.BigIntegerField(default=0)
    now_queue = models.BigIntegerField(default=0)


class medicinelist(models.Model):  #药品清单
    medicinelist_id = models.BigIntegerField(default=0)    #药品清单编号
    medicalrecord_id = models.BigIntegerField()   #对应的就诊表编号
    patient_id = models.BigIntegerField()
    name = models.CharField(max_length=200)
    price = models.BigIntegerField()
    number = models.BigIntegerField()

class queue(models.Model):  #排队
    depart = models.CharField(max_length=200)
    now_queue = models.BigIntegerField()
    queue = models.BigIntegerField()


from django.contrib import  admin
admin.site.register(patient)