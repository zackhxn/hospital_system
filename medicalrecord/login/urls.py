
from django.urls import path
from login.views import mainpage ,log_in_patient,register,log_in_doctor,log_in_manager,log_in_medicinemanager


urlpatterns = [

    path('',mainpage),  #登录页面
    path('log_in/patient/',log_in_patient),
    path('log_in/doctor/',log_in_doctor),
    path('log_in/manager/',log_in_manager),
    path('log_in/medicinemanager/',log_in_medicinemanager),
    path('register/',register)

]
