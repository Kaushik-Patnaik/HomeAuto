from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home),
    path('device/<str:pk>',views.getdevicestatus),
    path('device/<str:pk>/light1',views.togglelight1),
    path('device/<str:pk>/light2',views.togglelight2),
    path('device/<str:pk>/light3',views.togglelight3),
    path('device/<str:pk>/light4',views.togglelight4)

]
