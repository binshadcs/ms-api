from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import *
from .serializers import *

#Department,Venue,Time_set,Freezing_time,work_schedule
#DepartmentSerializer,VenueSerializer,Time_setSerializer,Freezing_timeSerializer,work_scheduleSerializer

@api_view(['GET'])
def overView(request):
    data ={
        "test" : "Dep",
        "test1" : "add_Dep/",
        "test3" : "update_Dep/<str:pk>/",
        "test4" : "delete_Dep/<str:pk>/",

        "test5" : "Venue",
        "test6" : "add_Venue",
        "test7" : "update_Venue/<str:pk>//",
        "test8" : "delete_Venue/<str:pk>/",

        "test9" : "Time_set",
        "test10" : "add_Time_set/",
        "test11" : "delete_Time_set/<str:pk>//",

        "test12" : "Freezing_time",
        "test13" : "add_Freezing_time",
        "test14" : "update_Freez/<str:pk>/",

        "test15" : "work_schedule/",
        "test16" : "getwork_schedule_detile/<str:pk>/",
        "test17" : "add_work_schedule/",
        "test18" : "update_work_schedule/<str:pk>/",
        "test19" : "delete_work_schedule/<str:pk>/",

        "test20" : "meeting/",
        "test21" : "meeting_detile/<str:pk>/",
        "test22" : "add_meeting/",
        "test23" : "update_meeting/<str:pk>/",
        "test24" : "delete_meeting/",

        "test25" : "participants/",
    }
    
    return Response(data)
#department detiles start here 
@api_view(['GET'])
def getData(request): 
    dep = Department.objects.all()
    serializer = DepartmentSerializer(dep, many=True)
    return Response(serializer.data)

@api_view(['POSt'])
def addDepartment(request):

    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POSt'])
def updateDepartment(request, pk):
    val = Department.objects.get(id=pk)
    serializer = DepartmentSerializer(instance=val, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteDepartment(request, pk):
    val = Department.objects.get(id=pk)
    val.delete()
    return Response("deleted succeccfully")
# department 

@api_view(['GET'])
def getVenue(request):
    venue = Venue.objects.all()
    serializer = VenueSerializer(venue, many=True)
    return Response(serializer.data)

@api_view(['POSt'])
def addVenue(request):
    serializer = VenueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POSt'])
def updateVenue(request, pk):
    val = Venue.objects.get(id=pk)
    serializer = VenueSerializer(instance=val, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteVenue(request, pk):
    val = Venue.objects.get(id=pk)
    val.delete()
    return Response("deleted succeccfully")

@api_view(['GET'])
def getTime_set(request):
    timeSet = Time_set.objects.all()
    serializer = Time_setSerializer(timeSet, many=True)
    return Response(serializer.data)

@api_view(['POSt'])
def addTime_set(request):
    serializer = Time_setSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTime_set(request, pk):
    val = Time_set.objects.get(id=pk)
    val.delete()
    return Response("deleted succeccfully")

@api_view(['GET'])
def getFreezing_time(request):
    frTime = Freezing_time.objects.all()
    serializer = Freezing_timeSerializer(frTime, many=True)
    return Response(serializer.data)

@api_view(['POSt'])
def addFreezing_time(request):
    serializer = Freezing_timeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POSt'])
def updateFreezing_time(request, pk):
    val = Freezing_time.objects.get(id=pk)
    serializer = Freezing_timeSerializer(instance=val, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#.filter(user=self.request.user)
@api_view(['GET'])
def getwork_schedule(request):
    wrk_s = work_schedule.objects.all()
    serializer = work_scheduleSerializer(wrk_s, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getwork_schedule_detile(request, pk):
    wrk_s = work_schedule.objects.get(id=pk)
    serializer = work_scheduleSerializer(wrk_s, many=False)
    return Response(serializer.data)

@api_view(['POSt'])
def addwork_schedule(request):
    serializer = work_scheduleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POSt'])
def updatework_schedule(request, pk):
    val = work_schedule.objects.get(id=pk)
    serializer = work_scheduleSerializer(instance=val, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletework_schedule(request, pk):
    val = work_schedule.objects.get(id=pk)
    val.delete()
    return Response("deleted succeccfully")

#meeting here
@api_view(['GET'])
def getmeeting(request):
    meet = meeting.objects.all()
    serializer = meetingSerializer(meet, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getmeeting_detile(request, pk):
    meet = meeting.objects.get(id=pk)
    serializer = meetingSerializer(meet, many=False)
    return Response(serializer.data)

@api_view(['POSt'])
def addmeeting(request):
    serializer = meetingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POSt'])
def updatemeeting(request, pk):
    val = meeting.objects.get(id=pk)
    serializer = meetingSerializer(instance=val, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletemeeting(request, pk):
    val = meeting.objects.get(id=pk)
    val.delete()
    return Response("deleted succeccfully")

#parcipants here
@api_view(['GET'])
def getParticipants(request):
    meet = Participants.objects.all()
    serializer = ParticipantsSerializer(meet, many=True)
    return Response(serializer.data)