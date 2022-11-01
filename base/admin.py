from django.contrib import admin
from base.models import Department,Freezing_time,Venue,Time_set, User,meeting, work_schedule, Participants

admin.site.register(Department)
admin.site.register(Freezing_time)
admin.site.register(Venue)
admin.site.register(Time_set)
admin.site.register(User)
admin.site.register(meeting)
admin.site.register(work_schedule)
admin.site.register(Participants)

# Register your models here.
