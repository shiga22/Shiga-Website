from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import UserProfileInfo,CourseProfileInfo,TaskInfo

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

       

        labels = {
        'password1':'Password',
        'password2':'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    intern = 'intern'
    student = 'student'
    employee = 'employee'
    user_types = [
        (intern, 'intern'),
        (student, 'student'),
        (employee,'employee'),
    ]
    user_type = forms.ChoiceField(required=True, choices=user_types)

    class Meta():
        model = UserProfileInfo
        fields = ('bio', 'profile_pic', 'user_type')
    

class CourseProfileInfoform(forms.ModelForm):
    name =forms.CharField(required=True)
    link =forms.CharField(required=True)
    coupon =forms.CharField(required=False)
    class Meta():
        model = CourseProfileInfo
        fields=('name','link','coupon') 

class TaskInfoform(forms.ModelForm):
    name =forms.CharField(required=True)
    link =forms.CharField(required=True)
    class Meta():
        model = TaskInfo
        fields=('name','link') 