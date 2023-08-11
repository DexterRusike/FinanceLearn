from django.urls import path
from . import views 

app_name = 'timesheet'

urlpatterns = [
    path('', views.submit_timesheet, name='submit_timesheet'),
]
