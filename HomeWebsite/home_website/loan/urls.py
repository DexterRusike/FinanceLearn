from django.urls import path
from . import views

app_name = 'loan'

urlpatterns = [
    path('', views.loan_application, name='loan_application')
]