from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Info
import os
from .MLModel import card_recognize
from django.conf import settings
from django.core.files.storage import FileSystemStorage


#Create your views here
@login_required(login_url="/login")
def home(response):
	if not Info.objects.filter(li=response.user).exists():
		if response.method=='POST':
			ph=response.POST['ph']
			email=response.POST['email']
			gender=response.POST['gender']
			new=Info(li=response.user,ph=ph,email=email,gender=gender)
			new.save()
			return redirect(pan)
		return render(response,'main/home.html')
	else:
		return redirect('components')



#to add pan card
@login_required(login_url="/login")
def pan(response):
	if response.method=='POST':
		file=response.FILES['file']
		fs = FileSystemStorage()
		filename = fs.save(file.name, file)
		uploaded_file_url = fs.url(filename)
		card,name,cardno=card_recognize(f'media/{filename}')
		return redirect(f'panvali/{card}/{name}/{cardno}/{filename}')
	return render(response,'main/pancard.html')



#for validating pancard
@login_required(login_url="/login")
def panvalidation(response,card,name,cardno,filename):
	if response.method=='POST':
		try:
			user=Info.objects.filter(li=response.user)[0]
			name=response.POST['name']
			cardno=response.POST['cardno']
			user.pancardno=cardno
			user.pancard=f'media/{filename}'
			user.save()
			return redirect(aadhar)
		except:
			return redirect(home)
	else:
		if card==2:
			return render(response,'main/pancardsub.html',{'cardno':cardno,'name':name})
		elif card==1:
			return render(response,'main/pancard.html',{'flag':1})
	


#for adding aadhar card
@login_required(login_url="/login")
def aadhar(response):
	if response.method=='POST':
		file=response.FILES['file']
		fs = FileSystemStorage()
		filename = fs.save(file.name, file)
		uploaded_file_url = fs.url(filename)
		card,name,cardno=card_recognize(f'media/{filename}')
		return redirect(f'aadharvali/{card}/{name}/{cardno}/{filename}')
	return render(response,'main/aadharcard.html')



#for validating aadhar card
@login_required(login_url='/login')
def aadharvalidation(response,card,name,cardno,filename):
	if response.method=='POST':
		try:
			user=Info.objects.filter(li=response.user)[0]
			name=response.POST['name']
			cardno=response.POST['cardno']
			user.aadharno=cardno
			user.aadhar=f'media/{filename}'
			user.save()
			return redirect(bankst)
		except:
			return redirect(home)
	else:
		if card==1:
			return render(response,'main/aadharsub.html',{'cardno':cardno,'name':name})
		elif card==2:
			return render(response,'main/aadharcard.html',{'flag':1})



#for adding bank statement
@login_required(login_url="/login")
def bankst(response):
	if response.method=='POST':
			user=Info.objects.filter(li=response.user)[0]
			file=response.FILES['file']
			user.bankst=file
			user.save()
			return redirect(photo)
	return render(response,'main/bankst.html')



@login_required(login_url="/login")
def photo(response):
	if response.method=='POST':
		user=Info.objects.filter(li=response.user)[0]
		file=response.FILES["file"]
		user.photo=file
		user.save()
		return redirect(components)
	return render(response,'main/photo.html')




#for viewing charts
@login_required(login_url='/login')
def charts(response):
	if Info.objects.filter(li=response.user).exists():
		return render(response,'main/charts.html')
	else:
		return redirect('home')



#for active stocks
@login_required(login_url='/login')
def stocks(response):
	if Info.objects.filter(li=response.user).exists():
		return render(response,'main/stocks.html')
	else:
		return redirect('home')



#for indices
@login_required(login_url="/login")
def indices(response):
	if Info.objects.filter(li=response.user).exists():
		return render(response,'main/indices.html')
	else:
		return redirect('home')


#for components
@login_required(login_url='/login')
def components(response):
	if Info.objects.filter(li=response.user).exists():
		return render(response,'main/components.html')
	else:
		return redirect('home')


#for stocks
@login_required(login_url="/login")
def globalmarket(response):
	if Info.objects.filter(li=response.user).exists():
		return render(response,'main/globalmarket.html')
	else:
		return redirect('home')


#for forex
@login_required(login_url="/login")
def forex(response):
	return render(response,'main/forex.html')


#for commodities
@login_required(login_url='/login')
def commidities(response):
	return render(response,'main/commodities.html')


#for cryptocurrencies
@login_required(login_url="/login")
def cryptocurrencies(response):
	return render(response,'main/cryptocurrencies.html')




def register(response):
	if response.method=="POST":
		form=UserCreationForm(response.POST)
		if form.is_valid():
			form.save()
			return render(response,"main/login.html")
	else:
		form=UserCreationForm()
	return render(response,'main/register.html',{'form':form})


