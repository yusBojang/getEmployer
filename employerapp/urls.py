from django.urls import path
from .views import *

urlpatterns = [
    path('emp', emp),
    path('showemp', showemp),
    path('', showemp),
    path('deleteEmp/<str:pk>', deleteEmp),
    path('editEmp/<str:pk>', editemp), 
    path('updateEmp/<str:pk>', updateEmp), 
]
