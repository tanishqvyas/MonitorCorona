from django.shortcuts import render
from .models import Country
from django.http import HttpResponse


import time

"""
import schedule
import time

def print_name():
	print("Tanishq")

schedule.every(10).seconds.do(print_name)

while 1:
	schedule.run_pending()
	time.sleep(1)

"""




# Create your views here.
def home_view(request,  *args, **kwargs):

	# # Faulty country list
	# faulty = {

	# 	"World":"xxx",
	# 	"Iran":"Iran, Islamic Republic of",
	# 	"Russia":"Russian Federation",
	# 	"S. Korea":"Korea, Republic of",
	# 	"Moldova":"Moldova, Republic of",
	# 	"Bolivia":"Bolivia, Plurinational State of",
	# 	"Kosovo":"xxx",
	# 	"Taiwan":"Taiwan, Province of China",
	# 	"Palestine":"Palestine, State of",
	# 	"Vietnam":"Viet Nam",
	# 	"DRC":"Congo, The Democratic Republic of the",
	# 	"Venezuela":"Venezuela, Bolivarian Republic of",
	# 	"Brunei ":"Brunei Darussalam",
	# 	"Republic of the Congo":"Congo, The Democratic Republic of the",
	# 	"Northern Cyprus":"Cyprus",
	# 	"Tanzania":"Tanzania, United Republic of",
	# 	"Myanmar":"Myanmar",
	# 	"Cabo Verde":"Cabo Verde",
	# 	"Sint Maarten":"Sint Maarten (Dutch part)",
	# 	"Bahamas":"Bahamas",
	# 	"Saint Martin":"xxx",
	# 	"Syria":"Syrian Arab Republic",
	# 	"Laos":"Lao People's Democratic Republic",
	# 	"Falkland Islands":"Falkland Islands (Malvinas)",
	# 	"Gambia":"Gambia",
	# 	"Vatican City":"xxx",
	# 	"British Virgin Islands":"Virgin Islands, British",
	# 	"India":"India",
	# 	"USA":"United States",
	# 	"Spain":"Spain",
	# 	"Italy":"Italy",
	# 	"Germany":"Germany",
	# 	"France":"France",
	# 	"UK":"United Kingdom",
	# 	"China":"China",
	# 	"Turkey":"Turkey",
	# 	"Belgium":"Belgium",
	# 	"Brazil":"Brazil",
	# 	"Canada":"Canada",
	# 	"Netherlands":"Netherlands",
	# 	"Switzerland":"Switzerland",
	# 	"Portugal":"Portugal",
	# 	"Austria":"Austria",
	# 	"Israel":"Israel",
	# 	"Ireland":"Ireland",
	# 	"Sweden":"Sweden",
	# 	"Peru":"Peru",
	# 	"Japan":"Japan",
	# 	"Chile":"Chile",
	# 	"Ecuador":"Ecuador",
	# 	"Poland":"Poland",
	# 	"Romania":"Romania",
	# 	"Denmark":"Denmark",
	# 	"Norway":"Norway",
	# 	"Pakistan":"Pakistan",
	# 	"Australia":"Australia",
	# 	"Czechia":"Czechia",
	# 	"Saudi Arabia":"Saudi Arabia",
	# 	"Mexico":"Mexico",
	# 	"Philippines":"Philippines",
	# 	"Indonesia":"Indonesia",
	# 	"UAE":"United Arab Emirates",
	# 	"Malaysia":"Malaysia",
	# 	"Serbia":"Serbia",
	# 	"Belarus":"Belarus",
	# 	"Ukraine":"Ukraine",
	# 	"Panama":"Panama",
	# 	"Qatar":"Qatar",
	# 	"Singapore":"Singapore",
	# 	"Dominican Republic":"Dominican Republic",
	# 	"Luxembourg":"Luxembourg",
	# 	"Finland":"Finland",
	# 	"Colombia":"Colombia",
	# 	"Thailand":"Thailand",
	# 	"South Africa":"South Africa",
	# 	"Egypt":"Egypt",
	# 	"Argentina":"Argentina",
	# 	"Greece":"Greece",
	# 	"Algeria":"Algeria",
	# 	"Morocco":"Morocco",
	# 	"Croatia":"Croatia",
	# 	"Iceland":"Iceland",
	# 	"Bahrain":"Bahrain",
	# 	"Hungary":"Hungary",
	# 	"Bangladesh":"Bangladesh",
	# 	"Estonia":"Estonia",
	# 	"Iraq":"Iraq",
	# 	"Kuwait":"Kuwait",
	# 	"Uzbekistan":"Uzbekistan",
	# 	"Kazakhstan":"Kazakhstan",
	# 	"Azerbaijan":"Azerbaijan",
	# 	"Slovenia":"Slovenia",
	# 	"Armenia":"Armenia",
	# 	"Lithuania":"Lithuania",
	# 	"New Zealand":"New Zealand",
	# 	"Oman":"Oman",
	# 	"Hong Kong":"Hong Kong",
	# 	"Slovakia":"Slovakia",
	# 	"North Macedonia":"North Macedonia",
	# 	"Cameroon":"Cameroon",
	# 	"Afghanistan":"Afghanistan",
	# 	"Cuba":"Cuba",
	# 	"Bulgaria":"Bulgaria",
	# 	"Tunisia":"Tunisia",
	# 	"Cyprus":"Cyprus",
	# 	"Latvia":"Latvia",
	# 	"Andorra":"Andorra",
	# 	"Lebanon":"Lebanon",
	# 	"Ivory Coast":"Côte d'Ivoire",
	# 	"Ghana":"Ghana",
	# 	"Costa Rica":"Costa Rica",
	# 	"Niger":"Niger",
	# 	"Burkina Faso":"Burkina Faso",
	# 	"Albania":"Albania",
	# 	"Uruguay":"Uruguay",
	# 	"Kyrgyzstan":"Kyrgyzstan",
	# 	"Djibouti":"Djibouti",
	# 	"Honduras":"Honduras",
	# 	"Nigeria":"Nigeria",
	# 	"Guinea":"Guinea",
	# 	"Jordan":"Jordan",
	# 	"Malta":"Malta",
	# 	"San Marino":"San Marino",
	# 	"Réunion":"Réunion",
	# 	"Georgia":"Georgia",
	# 	"Mauritius":"Mauritius",
	# 	"Senegal":"Senegal",
	# 	"Montenegro":"Montenegro",
	# 	"Isle of Man":"Isle of Man",
	# 	"Sri Lanka":"Sri Lanka",
	# 	"Mayotte":"Mayotte",
	# 	"Guernsey":"Guernsey",
	# 	"Kenya":"Kenya",
	# 	"Jersey":"Jersey",
	# 	"Guatemala":"Guatemala",
	# 	"Faroe Islands":"Faroe Islands",
	# 	"Paraguay":"Paraguay",
	# 	"El Salvador":"El Salvador",
	# 	"Martinique":"Martinique",
	# 	"Mali":"Mali",
	# 	"Guadeloupe":"Guadeloupe",
	# 	"Rwanda":"Rwanda",
	# 	"Gibraltar":"Gibraltar",
	# 	"Jamaica":"Jamaica",
	# 	"Cambodia":"Cambodia",
	# 	"Madagascar":"Madagascar",
	# 	"French Guiana":"French Guiana",
	# 	"Aruba":"Aruba",
	# 	"Monaco":"Monaco",
	# 	"Ethiopia":"Ethiopia",
	# 	"Bermuda":"Bermuda",
	# 	"Togo":"Togo",
	# 	"Gabon":"Gabon",
	# 	"Somalia":"Somalia",
	# 	"Liechtenstein":"Liechtenstein",
	# 	"Barbados":"Barbados",
	# 	"Cayman Islands":"Cayman Islands",
	# 	"French Polynesia":"French Polynesia",
	# 	"Guyana":"Guyana",
	# 	"Uganda":"Uganda",
	# 	"Equatorial Guinea":"Equatorial Guinea",
	# 	"Liberia":"Liberia",
	# 	"Libya":"Libya",
	# 	"Zambia":"Zambia",
	# 	"Guinea-Bissau":"Guinea-Bissau",
	# 	"Macao":"Macao",
	# 	"Haiti":"Haiti",
	# 	"Benin":"Benin",
	# 	"Eritrea":"Eritrea",
	# 	"Sudan":"Sudan",
	# 	"Mongolia":"Mongolia",
	# 	"Mozambique":"Mozambique",
	# 	"Chad":"Chad",
	# 	"Maldives":"Maldives",
	# 	"Zimbabwe":"Zimbabwe",
	# 	"Angola":"Angola",
	# 	"Belize":"Belize",
	# 	"New Caledonia":"New Caledonia",
	# 	"Timor-Leste":"Timor-Leste",
	# 	"Fiji":"Fiji",
	# 	"Dominica":"Dominica",
	# 	"Eswatini":"Eswatini",
	# 	"Malawi":"Malawi",
	# 	"Namibia":"Namibia",
	# 	"Nepal":"Nepal",
	# 	"Saint Lucia":"Saint Lucia",
	# 	"Curaçao":"Curaçao",
	# 	"Grenada":"Grenada",
	# 	"Botswana":"Botswana",
	# 	"Sierra Leone":"Sierra Leone",
	# 	"CAR":"Central African Republic",
	# 	"Greenland":"Greenland",
	# 	"Montserrat":"Montserrat",
	# 	"Seychelles":"Seychelles",
	# 	"Åland Islands":"Åland Islands",
	# 	"Suriname":"Suriname",
	# 	"Nicaragua":"Nicaragua",
	# 	"Mauritania":"Mauritania",
	# 	"St. Barth":"Saint Barthélemy",
	# 	"Bhutan":"Bhutan",
	# 	"Burundi":"Burundi",
	# 	"South Sudan":"South Sudan",
	# 	"Anguilla":"Anguilla",
	# 	"Papua New Guinea":"Papua New Guinea",
	# 	"Yemen":"Yemen",

	# 	"North America":"xxx",
	# 	"Asia":"xxx",
	# 	"Africa":"xxx",
	# 	"South America":"xxx",
	# 	"Europe":"xxx",
	# 	"Oceania":"xxx",
	# 	"":"xxx",
	# 	"Bosnia and Herzegovina":"Bosnia and Herzegovina",
	# 	"Diamond Princess":"xxx",
	# 	"Channel Islands":"xxx",
	# 	"Faeroe Islands":"Faroe Islands",
	# 	"Congo":"Congo",
	# 	"Trinidad and Tobago":"Trinidad and Tobago",
	# 	"Antigua and Barbuda":"Antigua and Barbuda",
	# 	"Saint Kitts and Nevis":"xxx",
	# 	"St. Vincent Grenadines":"xxx",
	# 	"Turks and Caicos":"Turks and Caicos Islands",
	# 	"MS Zaandam":"xxx",
	# 	"Western Sahara":"xxx",
	# 	"Sao Tome and Principe":"Sao Tome and Principe",
	# 	"Caribbean Netherlands":"xxx",
	# 	"Saint Pierre Miquelon":"Saint Pierre and Miquelon"

	# 	}

	# import requests
	# from bs4 import BeautifulSoup
	# import pycountry
	

	# url = "https://www.worldometers.info/coronavirus/"
	# r = requests.get(url)
	# soup = BeautifulSoup(r.content, 'html5lib')

	# # Opening a file to store data
	# file = open("/home/tanishq/MonitorCorona/track/public/data.csv","w")
	# file.write("ISO3,Name,2020\n")

	# # Get the table
	# table = soup.find("table", attrs = {'id':'main_table_countries_today'})

	# # Get table body
	# table_body = table.find("tbody")

	# # Get all the entries
	# table_entries = table_body.findAll("tr")
	# count = 0
	# print("Length  : ", len(table_entries))

	# for row in range(len(table_entries)):

	# 	# Find all data within each row
	# 	data = table_entries[row].findAll("td")

	# 	loc = data[0].text.strip("\n")
	# 	if(loc == ""):
	# 		continue

	# 	confirmed_cases = data[6].text.strip("\n").replace(",","")
	# 	cases_per_million = data[8].text.strip("\n").replace(",","")
	# 	recovered = data[5].text.strip("\n").replace(",","")
	# 	deaths = data[3].text.strip("\n").replace(",","")
		
	# 	if(cases_per_million==""):
	# 		cases_per_million="--"
	# 	if(recovered==""):
	# 		recovered="--"
	# 	if(deaths==" "):
	# 		deaths="--"


	# 	code="xxx"
	# 	# Getting ISO_A3 country code		
	# 	if(faulty[loc] != 'xxx'):

	# 		for i in pycountry.countries:
				
	# 			if(i.name == faulty[loc]):
	# 				# print(faulty[loc], i.name, count)
	# 				code = i.alpha_3
	# 				break

	# 	print(count)
	# 	count+=1
	# 	# Writing in the csv file
	# 	file.write(str(code)+","+str(loc)+","+str(confirmed_cases).replace(',','')+"\n")

	# 	# Getting flag url
	# 	url = "https://www.gstatic.com/onebox/sports/logos/flags/"
	# 	url += '_'.join(loc.lower().split())
	# 	url += "_icon_square"
	# 	url += '.png'

	# 	# Finding the entry :
	# 	entry = Country.objects.filter(country_name = loc)
		
	# 	# Checking if it exists
	# 	# Create if not else update
	# 	if len(entry) == 0:
	# 		# Country.objects.create(country_code = code, country_name = loc, confirmed_cases = confirmed_cases, cases_per_million = cases_per_million, total_recovered = recovered, total_deaths = deaths, url = url)
	# 		Country.objects.create(country_code = code, country_name = loc, confirmed_cases = confirmed_cases, cases_per_million = cases_per_million, total_recovered = recovered, total_deaths = deaths, url = url)
		
	# 	else:
	# 		entry.update(country_code = code)
	# 		entry.update(confirmed_cases = confirmed_cases)
	# 		entry.update(cases_per_million = cases_per_million)
	# 		entry.update(total_recovered = recovered)
	# 		entry.update(total_deaths = deaths)

	# # Closing the file
	# file.close()

	# Getting all the stuff from database
	query_results = Country.objects.all();

	# Creating a dictionary to pass as an argument
	context = {	'query_results' : query_results	}

	# Returning the rendered html
	return render(request, "home.html", context)

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})
