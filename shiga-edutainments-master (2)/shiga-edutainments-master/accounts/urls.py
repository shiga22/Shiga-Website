from django.urls import path
from . import views
urlpatterns=[
    path('',views.Index,name="index"),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('Course/',views.Course, name='course'),
    path('CourseDisplay',views.display, name='Course_Display'),
    path('Task/',views.Task, name='Task'),
    path('TaskDisplay',views.displayTask, name='task_Display'),
] 