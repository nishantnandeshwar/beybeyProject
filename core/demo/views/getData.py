from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from demo.models import DischargeBridgeMinuteData

@csrf_exempt
@api_view(('GET',))
def get_discharge_bridge_minute_list(request):
    discharge_bridge_minutes = DischargeBridgeMinuteData.objects.all()
    print(discharge_bridge_minutes)
    for minute in discharge_bridge_minutes:
        print(f'Timestamp: {minute.timestamp}')
        print(f'Record: {minute.record}')
        print(f'Battery Voltage Average: {minute.battv_avg}')
        print(f'System Temperature Average: {minute.system_temp_avg}')
        print(f'Temperature Average: {minute.temp_c_avg}')
        print(f'Water Velocity: {minute.water_velocity}')
        print(f'Water Column: {minute.water_column}')
        print(f'Signal Quality: {minute.signal_quality}')
        print(f'Water Discharge: {minute.water_discharge}')
        print('\n')
    discharge_bridge_data=[]
    for key in discharge_bridge_minutes.values('timestamp','record','battv_avg','system_temp_avg','temp_c_avg','water_velocity','water_column','signal_quality','water_discharge'):
        discharge_bridge_data.append(key)
    return JsonResponse({"data":discharge_bridge_data})