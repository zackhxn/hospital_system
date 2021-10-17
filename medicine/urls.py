
from django.urls import path
from medicine.views import show,submit


urlpatterns = [

    path('', show),  # 查看主页
    path('submit/',submit),

]
