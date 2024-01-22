# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('get-discharge-bridge-minutes/', views.getData.get_discharge_bridge_minute_list, name='get_discharge_bridge_minute_list'),
    path('discharge-bridge-minutes/', views.htmlView.discharge_bridge_minute_list,name='discharge_bridge_minute_list'),
    path('upload-file/',views.import_data.get_import_data,name='upload-file')
]
