from django.db import models
from phone_field import PhoneField


# Create your models here.
class Country(models.Model):

	country_code = models.CharField(max_length = 3, blank = False, null = False, default = '---')
	country_name = models.CharField(max_length = 120, blank = False, null = False, default ='--')
	confirmed_cases = models.CharField(max_length = 120, blank = False, null = False, default = '--')
	cases_per_million = models.CharField(max_length=120, blank = False, null = False, default = '--')
	total_recovered = models.CharField(max_length = 120, blank = False, null = False, default = '--')
	total_deaths = models.CharField(max_length = 120, blank = False, null = False, default = '--')
	url = models.CharField(max_length = 120, blank = True, null = False)