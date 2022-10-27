from dataclasses import field
from rest_framework import serializers
from base.models import Department,Venue,Time_set,Freezing_time,work_schedule,meeting,Participants

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

class work_scheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = work_schedule
        fields = '__all__'

class meetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = meeting
        fields = '__all__'

class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = '__all__'