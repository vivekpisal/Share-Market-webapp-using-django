from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Info(models.Model):
	li=models.OneToOneField(User,on_delete=models.CASCADE,related_name="info")
	ph=models.IntegerField(null=False,blank=False)
	email=models.EmailField(unique=True)
	gender=models.CharField(max_length=10)
	aadhar=models.ImageField(upload_to='images/aadhar/')
	aadharno=models.CharField(max_length=20,null=True)
	pancard=models.ImageField(upload_to='images/pancard/')
	pancardno=models.CharField(max_length=20,null=True)
	bankst=models.ImageField(upload_to='images/bankst/')
	photo=models.ImageField(upload_to='images/photo/')


	def __str__(self):
		return f'Email:{self.li}'
