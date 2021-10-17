
from django.urls import path
from mgr import patient

urlpatterns = [

    path('', patient.dispatcher),

]
