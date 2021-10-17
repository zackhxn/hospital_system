
from django.urls import path
from doctor.views import showdoctor,prescribe,update,select,selectpatient,generatelist


urlpatterns = [

    path('<int:id>/', showdoctor),  # 查看主页
    path('update/<int:id>', update),

    path('prescribe/', prescribe),
    path('select/<int:id>', select),
    path('selectpatient/<int:id>/<int:doctor_id>', selectpatient),
    path('generatelist/<int:id>', generatelist),   #生成药品清单表

]
