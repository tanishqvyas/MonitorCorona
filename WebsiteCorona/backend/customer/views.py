from django.shortcuts import HttpResponse, render, HttpResponseRedirect
from .models import Customer
from .forms import customer_form,rem_customer_form
from django.contrib import messages
from django.contrib.messages import constants as message_constants
import time

# Create your views here.
def new_customer(request):
	if request.method == "POST":
		form = customer_form(request.POST)
		if form.is_valid():
			form.save()	
			messages.add_message(request, message_constants.SUCCESS, '✔️ SUCCESSFUL SUBSCRIPTION')
			# time.sleep(0.5)
			return HttpResponseRedirect('http://127.0.0.1:8000/subscribe/')
			# return render(request,"new_customer.html",{'form':form})


	else:
		form = customer_form()
		
	return render(request,"new_customer.html",{'form':form})

def rem_customer(request):
	if request.method == "POST":
		form = rem_customer_form(request.POST)
		emailID = request.POST.get('email')
		exist = Customer.objects.filter(email = emailID).exists()
		if(exist == True):
			Customer.objects.filter(email = emailID).delete()
			messages.add_message(request, message_constants.SUCCESS, '✔️ UNSUBSCRIBED SUCCESSFULLY')
			return HttpResponseRedirect('http://127.0.0.1:8000/unsubscribe/')

		messages.add_message(request, message_constants.SUCCESS, '⚠️ User Does Not Exist')
		return HttpResponseRedirect('http://127.0.0.1:8000/unsubscribe/')


	else:
		form = rem_customer_form()
	return render(request,"rem_customer.html",{'form':form})

def about(request):
	# from corona.models import Country
	# country_data = Country.objects.values().filter(country_name="India")[0]
	# print(country_data["confirmed_cases"])

	# Message_str = "The current scenario of "+ "india" + " is, Confirmed Cases : " + str(country_data.confirmed_cases) + ", Total patients recovered : "+ str(country_data.total_recovered)+ ", Total number of deaths : "+str(country_data.total_deaths) 
	# print(Message_str)
	return render(request,"about.html",{})