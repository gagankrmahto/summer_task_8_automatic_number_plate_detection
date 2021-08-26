# Create your views here.
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import *
from . import pred
import xml.etree.ElementTree as ET
import requests
from . models import UploadImages
from django.http import HttpResponse
import json
from django.http import JsonResponse
import xmltodict
def index(request):
    number_plate = pred.show_results()
    print(number_plate)
    r = requests('https://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber=HR26DK8337&username=bitah')
    print(r.content)
    # tree = ET.parse('')
    # root = tree.getroot()
    # print(root)
    return render(request, 'main/car_display.html',{"num_plate":number_plate,"api_data":root})

def upload_the_car_image(request):
  
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            Cars = UploadImages.objects.values() 
        
            data = list(Cars)  # wrap in list(), because QuerySet is not JSON serializable
            
            cars_list=JsonResponse(data, safe=False) 
            print(type(data))
            # for d in data:
            #     print(d)
            car_url=f'media/{data[-1]["car_image"]}'
            print(type(car_url))
            print(type(cars_list))
            print(car_url)
            car_number=pred.get_car_number(car_url)
            print(car_number)
            r = requests.get("http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={0}&username=bitah".format(car_number))

            data = xmltodict.parse(r.content)
            jdata = json.dumps(data)
            df = json.loads(jdata)
            final_data = json.loads(df['Vehicle']['vehicleJson'])
            final_data['VechicleNumber'] = car_number
            print(type(final_data))
            print(final_data)
            # qs = UploadImages.objects.all()[::-1]
            # qs_json = serializers.serialize('json', qs)
            # print(type(qs_json))
            #     # return HttpResponse(qs_json, content_type='application/json')
            # print(qs_json)

            return render(request, 'main/car_display.html',{'my_dict' : final_data,'ImageUrl' : car_url })
    else:
        form = CarForm()
    return render(request, 'main/index.html',{"form":form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')


