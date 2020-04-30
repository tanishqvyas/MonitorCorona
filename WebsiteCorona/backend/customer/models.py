from django.utils.translation import ugettext as _
from django.db import models
from django import forms
# from django_countries.fields import CountryField

# COUNTRIES = (
#     ('GB', _('United Kingdom')), 
#     ('AF', _('Afghanistan')), 
#     ('AX', _('Aland Islands')), 
#     ('AL', _('Albania')), 
#     ('DZ', _('Algeria')), 
#     ('AS', _('American Samoa')), 
#     ('AD', _('Andorra')), 
#     ('AO', _('Angola')), 
#     ('AI', _('Anguilla')), 
#     ('AQ', _('Antarctica')), 
#     ('AG', _('Antigua and Barbuda')), 
#     ('AR', _('Argentina')), 
#     ('AM', _('Armenia')), 
#     ('AW', _('Aruba')), 
#     ('AU', _('Australia')), 
#     ('AT', _('Austria')), 
#     ('AZ', _('Azerbaijan')), 
#     ('BS', _('Bahamas')), 
#     ('BH', _('Bahrain')), 
#     ('BD', _('Bangladesh')), 
#     ('BB', _('Barbados')), 
#     ('BY', _('Belarus')), 
#     ('BE', _('Belgium')), 
#     ('BZ', _('Belize')), 
#     ('BJ', _('Benin')), 
#     ('BM', _('Bermuda')), 
#     ('BT', _('Bhutan')), 
#     ('BO', _('Bolivia')), 
#     ('BA', _('Bosnia and Herzegovina')), 
#     ('BW', _('Botswana')), 
#     ('BV', _('Bouvet Island')), 
#     ('BR', _('Brazil')), 
#     ('IO', _('British Indian Ocean Territory')), 
#     ('BN', _('Brunei Darussalam')), 
#     ('BG', _('Bulgaria')), 
#     ('BF', _('Burkina Faso')), 
#     ('BI', _('Burundi')), 
#     ('KH', _('Cambodia')), 
#     ('CM', _('Cameroon')), 
#     ('CA', _('Canada')), 
#     ('CV', _('Cape Verde')), 
#     ('KY', _('Cayman Islands')), 
#     ('CF', _('Central African Republic')), 
#     ('TD', _('Chad')), 
#     ('CL', _('Chile')), 
#     ('CN', _('China')), 
#     ('CX', _('Christmas Island')), 
#     ('CC', _('Cocos (Keeling) Islands')), 
#     ('CO', _('Colombia')), 
#     ('KM', _('Comoros')), 
#     ('CG', _('Congo')), 
#     ('CD', _('Congo, The Democratic Republic of the')), 
#     ('CK', _('Cook Islands')), 
#     ('CR', _('Costa Rica')), 
#     ('CI', _('Cote d\'Ivoire')), 
#     ('HR', _('Croatia')), 
#     ('CU', _('Cuba')), 
#     ('CY', _('Cyprus')), 
#     ('CZ', _('Czech Republic')), 
#     ('DK', _('Denmark')), 
#     ('DJ', _('Djibouti')), 
#     ('DM', _('Dominica')), 
#     ('DO', _('Dominican Republic')), 
#     ('EC', _('Ecuador')), 
#     ('EG', _('Egypt')), 
#     ('SV', _('El Salvador')), 
#     ('GQ', _('Equatorial Guinea')), 
#     ('ER', _('Eritrea')), 
#     ('EE', _('Estonia')), 
#     ('ET', _('Ethiopia')), 
#     ('FK', _('Falkland Islands (Malvinas)')), 
#     ('FO', _('Faroe Islands')), 
#     ('FJ', _('Fiji')), 
#     ('FI', _('Finland')), 
#     ('FR', _('France')), 
#     ('GF', _('French Guiana')), 
#     ('PF', _('French Polynesia')), 
#     ('TF', _('French Southern Territories')), 
#     ('GA', _('Gabon')), 
#     ('GM', _('Gambia')), 
#     ('GE', _('Georgia')), 
#     ('DE', _('Germany')), 
#     ('GH', _('Ghana')), 
#     ('GI', _('Gibraltar')), 
#     ('GR', _('Greece')), 
#     ('GL', _('Greenland')), 
#     ('GD', _('Grenada')), 
#     ('GP', _('Guadeloupe')), 
#     ('GU', _('Guam')), 
#     ('GT', _('Guatemala')), 
#     ('GG', _('Guernsey')), 
#     ('GN', _('Guinea')), 
#     ('GW', _('Guinea-Bissau')), 
#     ('GY', _('Guyana')), 
#     ('HT', _('Haiti')), 
#     ('HM', _('Heard Island and McDonald Islands')), 
#     ('VA', _('Holy See (Vatican City State)')), 
#     ('HN', _('Honduras')), 
#     ('HK', _('Hong Kong')), 
#     ('HU', _('Hungary')), 
#     ('IS', _('Iceland')), 
#     ('IN', _('India')), 
#     ('ID', _('Indonesia')), 
#     ('IR', _('Iran, Islamic Republic of')), 
#     ('IQ', _('Iraq')), 
#     ('IE', _('Ireland')), 
#     ('IM', _('Isle of Man')), 
#     ('IL', _('Israel')), 
#     ('IT', _('Italy')), 
#     ('JM', _('Jamaica')), 
#     ('JP', _('Japan')), 
#     ('JE', _('Jersey')), 
#     ('JO', _('Jordan')), 
#     ('KZ', _('Kazakhstan')), 
#     ('KE', _('Kenya')), 
#     ('KI', _('Kiribati')), 
#     ('KP', _('Korea, Democratic People\'s Republic of')), 
#     ('KR', _('Korea, Republic of')), 
#     ('KW', _('Kuwait')), 
#     ('KG', _('Kyrgyzstan')), 
#     ('LA', _('Lao People\'s Democratic Republic')), 
#     ('LV', _('Latvia')), 
#     ('LB', _('Lebanon')), 
#     ('LS', _('Lesotho')), 
#     ('LR', _('Liberia')), 
#     ('LY', _('Libyan Arab Jamahiriya')), 
#     ('LI', _('Liechtenstein')), 
#     ('LT', _('Lithuania')), 
#     ('LU', _('Luxembourg')), 
#     ('MO', _('Macao')), 
#     ('MK', _('Macedonia, The Former Yugoslav Republic of')), 
#     ('MG', _('Madagascar')), 
#     ('MW', _('Malawi')), 
#     ('MY', _('Malaysia')), 
#     ('MV', _('Maldives')), 
#     ('ML', _('Mali')), 
#     ('MT', _('Malta')), 
#     ('MH', _('Marshall Islands')), 
#     ('MQ', _('Martinique')), 
#     ('MR', _('Mauritania')), 
#     ('MU', _('Mauritius')), 
#     ('YT', _('Mayotte')), 
#     ('MX', _('Mexico')), 
#     ('FM', _('Micronesia, Federated States of')), 
#     ('MD', _('Moldova')), 
#     ('MC', _('Monaco')), 
#     ('MN', _('Mongolia')), 
#     ('ME', _('Montenegro')), 
#     ('MS', _('Montserrat')), 
#     ('MA', _('Morocco')), 
#     ('MZ', _('Mozambique')), 
#     ('MM', _('Myanmar')), 
#     ('NA', _('Namibia')), 
#     ('NR', _('Nauru')), 
#     ('NP', _('Nepal')), 
#     ('NL', _('Netherlands')), 
#     ('AN', _('Netherlands Antilles')), 
#     ('NC', _('New Caledonia')), 
#     ('NZ', _('New Zealand')), 
#     ('NI', _('Nicaragua')), 
#     ('NE', _('Niger')), 
#     ('NG', _('Nigeria')), 
#     ('NU', _('Niue')), 
#     ('NF', _('Norfolk Island')), 
#     ('MP', _('Northern Mariana Islands')), 
#     ('NO', _('Norway')), 
#     ('OM', _('Oman')), 
#     ('PK', _('Pakistan')), 
#     ('PW', _('Palau')), 
#     ('PS', _('Palestinian Territory, Occupied')), 
#     ('PA', _('Panama')), 
#     ('PG', _('Papua New Guinea')), 
#     ('PY', _('Paraguay')), 
#     ('PE', _('Peru')), 
#     ('PH', _('Philippines')), 
#     ('PN', _('Pitcairn')), 
#     ('PL', _('Poland')), 
#     ('PT', _('Portugal')), 
#     ('PR', _('Puerto Rico')), 
#     ('QA', _('Qatar')), 
#     ('RE', _('Reunion')), 
#     ('RO', _('Romania')), 
#     ('RU', _('Russian Federation')), 
#     ('RW', _('Rwanda')), 
#     ('BL', _('Saint Barthelemy')), 
#     ('SH', _('Saint Helena')), 
#     ('KN', _('Saint Kitts and Nevis')), 
#     ('LC', _('Saint Lucia')), 
#     ('MF', _('Saint Martin')), 
#     ('PM', _('Saint Pierre and Miquelon')), 
#     ('VC', _('Saint Vincent and the Grenadines')), 
#     ('WS', _('Samoa')), 
#     ('SM', _('San Marino')), 
#     ('ST', _('Sao Tome and Principe')), 
#     ('SA', _('Saudi Arabia')), 
#     ('SN', _('Senegal')), 
#     ('RS', _('Serbia')), 
#     ('SC', _('Seychelles')), 
#     ('SL', _('Sierra Leone')), 
#     ('SG', _('Singapore')), 
#     ('SK', _('Slovakia')), 
#     ('SI', _('Slovenia')), 
#     ('SB', _('Solomon Islands')), 
#     ('SO', _('Somalia')), 
#     ('ZA', _('South Africa')), 
#     ('GS', _('South Georgia and the South Sandwich Islands')), 
#     ('ES', _('Spain')), 
#     ('LK', _('Sri Lanka')), 
#     ('SD', _('Sudan')), 
#     ('SR', _('Suriname')), 
#     ('SJ', _('Svalbard and Jan Mayen')), 
#     ('SZ', _('Swaziland')), 
#     ('SE', _('Sweden')), 
#     ('CH', _('Switzerland')), 
#     ('SY', _('Syrian Arab Republic')), 
#     ('TW', _('Taiwan, Province of China')), 
#     ('TJ', _('Tajikistan')), 
#     ('TZ', _('Tanzania, United Republic of')), 
#     ('TH', _('Thailand')), 
#     ('TL', _('Timor-Leste')), 
#     ('TG', _('Togo')), 
#     ('TK', _('Tokelau')), 
#     ('TO', _('Tonga')), 
#     ('TT', _('Trinidad and Tobago')), 
#     ('TN', _('Tunisia')), 
#     ('TR', _('Turkey')), 
#     ('TM', _('Turkmenistan')), 
#     ('TC', _('Turks and Caicos Islands')), 
#     ('TV', _('Tuvalu')), 
#     ('UG', _('Uganda')), 
#     ('UA', _('Ukraine')), 
#     ('AE', _('United Arab Emirates')), 
#     ('US', _('United States')), 
#     ('UM', _('United States Minor Outlying Islands')), 
#     ('UY', _('Uruguay')), 
#     ('UZ', _('Uzbekistan')), 
#     ('VU', _('Vanuatu')), 
#     ('VE', _('Venezuela')), 
#     ('VN', _('Viet Nam')), 
#     ('VG', _('Virgin Islands, British')), 
#     ('VI', _('Virgin Islands, U.S.')), 
#     ('WF', _('Wallis and Futuna')), 
#     ('EH', _('Western Sahara')), 
#     ('YE', _('Yemen')), 
#     ('ZM', _('Zambia')), 
#     ('ZW', _('Zimbabwe')), 
# )


COUNTRIES = (

    ('Afghanistan', _('Afghanistan')),

    ('Albania', _('Albania')),

    ('Algeria', _('Algeria')),

    ('Andorra', _('Andorra')),

    ('Angola', _('Angola')),

    ('Anguilla', _('Anguilla')),

    ('Antigua and Barbuda', _('Antigua and Barbuda')),

    ('Argentina', _('Argentina')),

    ('Armenia', _('Armenia')),

    ('Aruba', _('Aruba')),

    ('Australia', _('Australia')),

    ('Austria', _('Austria')),

    ('Azerbaijan', _('Azerbaijan')),

    ('Bahrain', _('Bahrain')),

    ('Bangladesh', _('Bangladesh')),

    ('Barbados', _('Barbados')),

    ('Belarus', _('Belarus')),

    ('Belgium', _('Belgium')),

    ('Belize', _('Belize')),

    ('Benin', _('Benin')),

    ('Bermuda', _('Bermuda')),

    ('Bhutan', _('Bhutan')),

    ('Bolivia', _('Bolivia')),

    ('Bosnia and Herzegovina', _('Bosnia and Herzegovina')),

    ('Botswana', _('Botswana')),

    ('Brazil', _('Brazil')),

    ('British Virgin Islands', _('British Virgin Islands')),

    ('Brunei', _('Brunei')),

    ('Bulgaria', _('Bulgaria')),

    ('Burkina Faso', _('Burkina Faso')),

    ('Burundi', _('Burundi')),

    ('Cambodia', _('Cambodia')),

    ('Cameroon', _('Cameroon')),

    ('Canada', _('Canada')),

    ('Cape Verde', _('Cape Verde')),

    ('Cayman Islands', _('Cayman Islands')),

    ('Central African Republic', _('Central African Republic')),

    ('Chad', _('Chad')),

    ('Chile', _('Chile')),

    ('China', _('China')),

    ('Colombia', _('Colombia')),

    ('Costa Rica', _('Costa Rica')),

    ('Croatia', _('Croatia')),

    ('Cuba', _('Cuba')),

              ('Curaçao',_('Curaçao')),

              ('Cyprus', _('Cyprus')),

    ('Czechia', _('Czechia')),

              ('Côte d\'Ivoire', _('Côte d\'Ivoire')),

              ('Democratic Republic of the Congo',_('Democratic Republic of the Congo')),

    ('Denmark', _('Denmark')),

    ('Djibouti', _('Djibouti')),

    ('Dominica', _('Dominica')),

    ('Dominican Republic', _('Dominican Republic')),

    ('Ecuador', _('Ecuador')),

    ('Egypt', _('Egypt')),

    ('El Salvador', _('El Salvador')),

    ('Equatorial Guinea', _('Equatorial Guinea')),

    ('Eritrea', _('Eritrea')),

    ('Estonia', _('Estonia')),

    ('Ethiopia', _('Ethiopia')),

              ('Eswatini',_('Eswatini')),

    ('Falkland Islands (Islas Malvinas)', _('Falkland Islands (Islas Malvinas)')),

    ('Faroe Islands', _('Faroe Islands')),

    ('Fiji', _('Fiji')),

    ('Finland', _('Finland')),

    ('France', _('France')),

    ('French Guiana', _('French Guiana')),

    ('French Polynesia', _('French Polynesia')),

    ('Gabon', _('Gabon')),

    ('Georgia', _('Georgia')),

    ('Germany', _('Germany')),

    ('Ghana', _('Ghana')),

    ('Gibraltar', _('Gibraltar')),

    ('Greece', _('Greece')),

    ('Greenland', _('Greenland')),

    ('Grenada', _('Grenada')),

    ('Guadeloupe', _('Guadeloupe')),

    ('Guatemala', _('Guatemala')),

    ('Guernsey', _('Guernsey')),

    ('Guinea', _('Guinea')),

    ('Guinea-Bissau', _('Guinea-Bissau')),

    ('Guyana', _('Guyana')),

    ('Haiti', _('Haiti')),

    ('Honduras', _('Honduras')),

    ('Hong Kong', _('Hong Kong')),

    ('Hungary', _('Hungary')),

    ('Iceland', _('Iceland')),

    ('India', _('India')),

    ('Indonesia', _('Indonesia')),

    ('Iran', _('Iran')),

    ('Iraq', _('Iraq')),

    ('Ireland', _('Ireland')),

    ('Isle of Man', _('Isle of Man')),

    ('Israel', _('Israel')),

    ('Italy', _('Italy')),

    ('Jamaica', _('Jamaica')),

    ('Japan', _('Japan')),

    ('Jersey', _('Jersey')),

    ('Jordan', _('Jordan')),

    ('Kazakhstan', _('Kazakhstan')),

    ('Kenya', _('Kenya')),

    ('Kosovo', _('Kosovo')),

    ('Kuwait', _('Kuwait')),

    ('Kyrgyzstan', _('Kyrgyzstan')),

    ('Laos', _('Laos')),

    ('Latvia', _('Latvia')),

    ('Lebanon', _('Lebanon')),

    ('Liberia', _('Liberia')),

    ('Libya', _('Libya')),

    ('Liechtenstein', _('Liechtenstein')),

    ('Lithuania', _('Lithuania')),

    ('Luxembourg', _('Luxembourg')),

    ('Macao', _('Macao')),

    ('Madagascar', _('Madagascar')),

    ('Malawi', _('Malawi')),

    ('Malaysia', _('Malaysia')),

    ('Maldives', _('Maldives')),

    ('Mali', _('Mali')),

    ('Malta', _('Malta')),

    ('Martinique', _('Martinique')),

    ('Mauritania', _('Mauritania')),

    ('Mauritius', _('Mauritius')),

    ('Mayotte', _('Mayotte')),

    ('Mexico', _('Mexico')),

    ('Moldova', _('Moldova')),

    ('Monaco', _('Monaco')),

    ('Mongolia', _('Mongolia')),

    ('Montenegro', _('Montenegro')),

    ('Montserrat', _('Montserrat')),

    ('Morocco', _('Morocco')),

    ('Mozambique', _('Mozambique')),

    ('Myanmar (Burma)', _('Myanmar (Burma)')),

    ('Namibia', _('Namibia')), 

    ('Nepal', _('Nepal')),

    ('Netherlands', _('Netherlands')),

    ('New Caledonia', _('New Caledonia')),

    ('New Zealand', _('New Zealand')),

    ('Nicaragua', _('Nicaragua')),

    ('Niger', _('Niger')),

    ('Nigeria', _('Nigeria')),

    ('North Macedonia', _('North Macedonia')),

    ('Northern Cyprus', _('Northern Cyprus')),

    ('Norway', _('Norway')),

    ('Oman', _('Oman')),

    ('Pakistan', _('Pakistan')),

    ('Palestine', _('Palestine')),

    ('Panama', _('Panama')),

    ('Papua New Guinea', _('Papua New Guinea')),

    ('Paraguay', _('Paraguay')),

    ('Peru', _('Peru')),

    ('Philippines', _('Philippines')),

    ('Poland', _('Poland')),

    ('Portugal', _('Portugal')),

    ('Qatar', _('Qatar')),

              ('Republic of the Congo',_('Republic of the Congo')),

    ('Réunion', _('Réunion')),

    ('Romania', _('Romania')),

    ('Russia', _('Russia')),

    ('Rwanda', _('Rwanda')),

    ('Saint Barthélemy', _('Saint Barthélemy')),

    ('Saint Kitts and Nevis', _('Saint Kitts and Nevis')),

    ('Saint Lucia', _('Saint Lucia')),

    ('Saint Martin', _('Saint Martin')),

    ('Saint Pierre and Miquelon', _('Saint Pierre and Miquelon')),

    ('San Marino', _('San Marino')),

    ('Saudi Arabia', _('Saudi Arabia')),

    ('Senegal', _('Senegal')),

    ('Serbia', _('Serbia')),

    ('Seychelles', _('Seychelles')),

    ('Sierra Leone', _('Sierra Leone')),

    ('Singapore', _('Singapore')),

              ('Sint Maarten',_('Sint Maarten')),

    ('Slovakia', _('Slovakia')),

    ('Slovenia', _('Slovenia')),

    ('Somalia', _('Somalia')),

    ('South Africa', _('South Africa')),

    ('South Korea', _('South Korea')),

              ('South Sudan',_('South Sudan')),

    ('Spain', _('Spain')),

    ('Sri Lanka', _('Sri Lanka')),

    ('Sudan', _('Sudan')),

    ('Suriname', _('Suriname')),

    ('Sweden', _('Sweden')),

    ('Switzerland', _('Switzerland')),

    ('Syria', _('Syria')),

              ('São Tomé and Príncipe',_('São Tomé and Príncipe')),

    ('Taiwan', _('Taiwan')),

    ('Tanzania', _('Tanzania')),

    ('Thailand', _('Thailand')),

              ('The Bahamas', _('The Bahamas')),

    ('The Gambia', _('The Gambia')),

    ('Timor-Leste', _('Timor-Leste')),

    ('Togo', _('Togo')),

    ('Trinidad and Tobago', _('Trinidad and Tobago')),

    ('Tunisia', _('Tunisia')),

    ('Turkey', _('Turkey')),

    ('Turks and Caicos Islands', _('Turks and Caicos Islands')),

    ('Uganda', _('Uganda')),

    ('Ukraine', _('Ukraine')),

    ('United Arab Emirates', _('United Arab Emirates')),

              ('United Kingdom', _('United Kingdom')),

    ('United States', _('United States')),

    ('Uruguay', _('Uruguay')),

    ('Uzbekistan', _('Uzbekistan')),

    ('Vatican City', _('Vatican City')),

    ('Venezuela', _('Venezuela')),

    ('Vietnam', _('Vietnam')),

    ('Yemen', _('Yemen')),

    ('Zambia', _('Zambia')),

    ('Zimbabwe', _('Zimbabwe')),

              ('Åland Islands', _('Åland Islands')),

)


# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length = 20, blank=False,null=False)
	email = models.EmailField(max_length = 254,blank=False,null=False,unique=True)
	country = models.CharField(max_length = 254,null=False,blank=False, default="India" , choices = COUNTRIES)
	class Meta:  
		db_table = "customer"