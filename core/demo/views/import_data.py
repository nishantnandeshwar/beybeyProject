# your_app/management/commands/import_data.py
import csv
from django.core.management.base import BaseCommand
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from demo.models import DischargeBridgeMinuteData
from datetime import datetime

@csrf_exempt
@api_view(('POST',))
def get_import_data(request):
    uploaded_file = request.FILES.get('csv_file', None)
    print("uploaded_file>>",uploaded_file)

    # Process the CSV file
    try:
        decoded_file = uploaded_file.read().decode('utf-8')
        csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
                
        # Assuming the first row contains headers, skip it
        headers = next(csv_data)

        # Process each row in the CSV file
        for row in csv_data:
            instance = DischargeBridgeMinuteData.objects.create(
            timestamp=str(datetime.strptime(row[0], '%d-%m-%Y %H:%M')),
            # timestamp='2024-01-13 17:15:00',
            record=row[1],
            battv_avg=row[2],
            system_temp_avg=row[3],
            temp_c_avg=row[4],
            water_velocity=row[5],
            water_column=row[6],
            signal_quality=row[7],
            water_discharge=row[8],
            )
        for row in csv_data:
            # print("row>>",row[0])
            print("row>>",str(datetime.strptime(row[0], '%d-%m-%Y %H:%M')))
        return JsonResponse({'message': 'CSV file uploaded and processed successfully'})
    except Exception as e:
        return JsonResponse({'error': f'Error processing CSV file: {str(e)}'}, status=500)
    
        