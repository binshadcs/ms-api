from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Department,Venue,Time_set,Freezing_time
from .serializers import DepartmentSerializer,VenueSerializer,Time_setSerializer,Freezing_timeSerializer

@api_view(['GET'])
def overView(request):
    #this function for getting data of department 
    data ={
        "test" : "name",
        "test1" : "check",
        "test2" : "saample",
    }
    
    return Response(data)

@api_view(['GET'])
def getData(request):
    #this function for getting data of department 
    dep = Department.objects.all()
    serializer = DepartmentSerializer(dep, many=True)
    return Response(serializer.data)

@api_view(['POSt'])
def addDepartment(request):

    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getVenue(request):
    #this function for getting data of department 
    venue = Venue.objects.all()
    serializer = VenueSerializer(venue, many=True)
    return Response(serializer.data)

@api_view(['POSt'])
def addVenue(request):
    serializer = VenueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

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