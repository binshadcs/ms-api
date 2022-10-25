from dataclasses import field
from rest_framework import serializers
from base.models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
