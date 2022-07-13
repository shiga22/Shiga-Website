from django.contrib import admin
from accounts.models import UserProfileInfo,CourseProfileInfo,TaskInfo
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(CourseProfileInfo)
admin.site.register(TaskInfo)