from django.urls import path
from . import views

urlpatterns = [
    path('',views.overView),
    path('Dep',views.getData),#getdata about getting department detiles from model
    path('add_Dep',views.addDepartment),
    path('update_Dep/<str:pk>/',views.updateDepartment),
    path('delete_Dep/<str:pk>/',views.deleteDepartment),

    path('Venue',views.getVenue),
    path('add_Venue',views.addVenue),
    path('delete_Venue/<str:pk>/',views.deleteVenue),
    path('update_Venue/<str:pk>/',views.updateVenue),

    path('Time_set',views.getTime_set),
    path('add_Time_set',views.addTime_set),
    path('delete_Time_set/<str:pk>/',views.deleteTime_set),

    path('Freezing_time',views.getFreezing_time),
    path('add_Freezing_time',views.addFreezing_time),
    path('update_Freez/<str:pk>/',views.updateFreezing_time),

    path('work_schedule/',views.getwork_schedule),
    path('getwork_schedule_detile/<str:pk>/',views.getwork_schedule_detile),
    path('add_work_schedule/',views.addwork_schedule),
    path('update_work_schedule/<str:pk>/',views.updatework_schedule),
    path('delete_work_schedule/<str:pk>/',views.updatework_schedule),

    path('meeting/',views.getmeeting),
    path('meeting_detile/<str:pk>/',views.getmeeting_detile),
    path('add_meeting/',views.addmeeting),
    path('update_meeting/<str:pk>/',views.updatemeeting),
    path('delete_meeting/',views.deletemeeting),

    path('participants/',views.getParticipants),

]