
from django.urls import path
from patient.views import showpatient,register,update,record


urlpatterns = [

    path('<int:id>/',showpatient),  #查看主页

    path('update/<int:id>', update), #修改信息
    path('register/<int:id>',register),  #挂号
    path('record/<int:id>',record),  #挂号
]
