from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Department
from .serializers import DepartmentSerializer

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