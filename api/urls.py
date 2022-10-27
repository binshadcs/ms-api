from django.urls import path
from . import views

urlpatterns = [
    path('',views.overView),
    path('Dep',views.getData),#getdata about getting department detiles from model
    path('addDep',views.addDepartment),
    path('updateDep/<str:pk>/',views.updateDepartment),
    path('deleteDep/<str:pk>/',views.deleteDepartment),

    path('Venue',views.getVenue),
    path('addVenue',views.addVenue),
    path('deleteVenue/<str:pk>',views.deleteVenue),

    path('Time_set',views.getTime_set),
    path('addTime_set',views.addTime_set),
    path('deleteTime_set/<str:pk>',views.deleteTime_set),

    path('Freezing_time',views.getFreezing_time),
    path('addFreezing_time',views.addFreezing_time),
    path('updateFreez/<str:pk>/',views.updateFreezing_time),
]