from django.urls import path
from . views import *
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.index, name='index'),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('register/',Registeration.as_view(), name='register'),
     path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('delete/<int:id>/',views.delete_consumed_food, name='delete')
    
]