from . import views 
from django.urls import path


urlpatterns = [

path('', views.current_datetime, name="index")

]