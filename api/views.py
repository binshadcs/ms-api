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