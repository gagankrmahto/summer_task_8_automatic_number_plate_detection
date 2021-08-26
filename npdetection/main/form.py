# forms.py
from django import forms
from .models import *

class CarForm(forms.ModelForm):

	class Meta:
		model = UploadImages
		fields = ['car_image']
