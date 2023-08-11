from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('user_login/',views.user_login, name='user_login'),
    
]