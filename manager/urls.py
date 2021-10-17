
from django.urls import path
from manager.views import show , submitpatient , submitdoctor , updatepatient , updatedoctor , deletepatient ,deletedoctor


urlpatterns = [


    path('', show),
    path('submitpatient/', submitpatient),
    path('submitdoctor/', submitdoctor),
    path('updatepatient/<int:id>',updatepatient),
    path('updatedoctor/<int:id>',updatedoctor),
    path('deletepatient/<int:id>',deletepatient),
    path('deletedoctor/<int:id>',deletedoctor),

]