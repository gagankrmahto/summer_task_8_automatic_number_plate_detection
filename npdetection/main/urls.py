from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path('', views.upload_the_car_image, name='car_image_upload'),
    path('success', success, name = 'success'),
    path('display', views.index, name = 'success'),
]