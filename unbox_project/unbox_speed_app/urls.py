from django.urls import path 
from .views import  SpeedDataViewSet

urlpatterns = [ 
    #This API showing list of speed and timestamp objects
    path('speedlist/', SpeedDataViewSet.as_view({'get': 'get_data'}), name='speedometer-data'),

    #This API showing speed at intervals 
    path('speedlistatintervals/', SpeedDataViewSet.as_view({'get': 'create_data_at_intervals'}), name='speedometerinterval-data'),
] 
