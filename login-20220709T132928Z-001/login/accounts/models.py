from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)
    
class UserProfileInfo(models.Model):

    #creating a relationship with user class (not inheriting)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #adding additional attributes
    bio = models.CharField(max_length=500)
    profile_pic = models.ImageField(upload_to=path_and_rename,verbose_name="Profile Picture", blank=True)
    intern = 'intern'
    student = 'student'
    employee = 'employee'
    user_types = [
        (intern, 'intern'),
        (student, 'student'),
        (employee, 'employee'),
    ]
    user_type = models.CharField(max_length=10, choices=user_types, default=student)
    def __str__(self):
        return self.user.username


class CourseProfileInfo( models.Model):
    name =models.CharField(max_length=100,blank=False)
    link =models.CharField(max_length=100)
    coupon =models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class TaskInfo( models.Model):
    name =models.CharField(max_length=100,blank=False)
    link =models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)