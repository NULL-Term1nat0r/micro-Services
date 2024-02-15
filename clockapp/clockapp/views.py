from django.shortcuts import render
from django.http import JsonResponse
import datetime
import time

def clock(request):
    return render(request, 'clock.html')

def get_time(request):
    current_time = time.strftime('%H:%M:%S')
    return JsonResponse({'time': current_time})