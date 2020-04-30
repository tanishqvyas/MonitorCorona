from django import forms
from .models import Customer
class customer_form(forms.ModelForm):
	class Meta:
		model = Customer
		fields = "__all__"

class rem_customer_form(forms.ModelForm):
	class Meta:
		model = Customer
		fields = [
			'email'
		]
