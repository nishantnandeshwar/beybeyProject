from django.shortcuts import render

# Create your views here.
# views.py
from demo.models import DischargeBridgeMinuteData

def discharge_bridge_minute_list(request):
    # Retrieve all objects from the DischargeBridgeMinute model
    discharge_bridge_minutes = DischargeBridgeMinuteData.objects.all()

    # Pass the data to the template for rendering
    return render(request, 'demo/discharge_bridge_minute_list.html', {'discharge_bridge_minutes': discharge_bridge_minutes})
