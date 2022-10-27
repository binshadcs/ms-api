from dataclasses import field
from rest_framework import serializers
from base.models import Department,Venue,Time_set,Freezing_time

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'

class Time_setSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time_set
        fields = '__all__'


class Freezing_timeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freezing_time
        fields = '__all__'