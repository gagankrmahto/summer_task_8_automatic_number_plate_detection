from django.db import models

# Create your models here.
# models.py
class UploadImages(models.Model):
	name = models.CharField(max_length=50)
	car_image = models.ImageField(upload_to='images/')
