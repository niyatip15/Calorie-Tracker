from django.urls import path
from . views import *
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('delete/<int:id>/',views.delete_consumed_food, name='delete')
    
]