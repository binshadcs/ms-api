from django.urls import path
from . import views

urlpatterns = [
    path('',views.overView),
    path('dep',views.getData),#getdata about geting department detiles from model
    path('dep/add',views.addDepartment),
    path('venue',views.getVenue),
    path('venue/add',views.addVenue),
    path('time_set',views.getTime_set),
    path('time_set/add',views.addTime_set),
    path('freezing_time',views.getFreezing_time),
    path('freezing_time/add',views.addFreezing_time),
]