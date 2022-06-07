from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Device,UserDevice



# Create your views here.
def home(request):
    return HttpResponse("this is home")

def getdevicestatus(request,pk):
    try:
        device=Device.objects.get(deviceId=pk)
        dict_= {'device':device.deviceId,
        'l1':device.lightStatus1,
        'l2':device.lightStatus2,
        'l3':device.lightStatus3,
        'l4':device.lightStatus4}
        return JsonResponse(dict_)

    except Device.DoesNotExist:
        return JsonResponse({'message':'no devices found'})

def togglelight1(request,pk):
    try:
        device=Device.objects.get(deviceId=pk)
        if device.lightStatus1==0:

            device.lightStatus1=1
        else:
            device.lightStatus1=0
        device.save()
        dict_={'deviceId':device.deviceId,'light':device.lightStatus1}
        return JsonResponse(dict_)

    except Device.DoesNotExist:
        return JsonResponse({'message':'no devices found'})

def togglelight2(request,pk):
    try:
        device=Device.objects.get(deviceId=pk)
        if device.lightStatus2==0:

            device.lightStatus2=1
        else:
            device.lightStatus2=0
        device.save()
        dict_={'deviceId':device.deviceId,'light':device.lightStatus2}
        return JsonResponse(dict_)

    except Device.DoesNotExist:
        return JsonResponse({'message':'no devices found'})

def togglelight3(request,pk):
    try:
        device=Device.objects.get(deviceId=pk)
        if device.lightStatus3==0:

            device.lightStatus3=1
        else:
            device.lightStatus3=0
        device.save()
        dict_={'deviceId':device.deviceId,'light':device.lightStatus3}
        return JsonResponse(dict_)

    except Device.DoesNotExist:
        return JsonResponse({'message':'no devices found'})

def togglelight4(request,pk):
    try:
        device=Device.objects.get(deviceId=pk)
        if device.lightStatus4==0:

            device.lightStatus4=1
        else:
            device.lightStatus4=0
        device.save()
        dict_={'deviceId':device.deviceId,'light':device.lightStatus4}
        return JsonResponse(dict_)

    except Device.DoesNotExist:
        return JsonResponse({'message':'no devices found'})