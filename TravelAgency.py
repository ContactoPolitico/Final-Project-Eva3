import requests

country = input("Choose the country you want to visit: ").capitalize()

linkcountry = f"https://www.apicountries.com/name/{country}"

response = requests.get(linkcountry)

name = response.json()[0]["name"]
latitude = response.json()[0]["latlng"][0]
longitude = response.json()[0]["latlng"][1]
capital = response.json()[0]["capital"]
region = response.json()[0]["region"]
subregion = response.json()[0]["subregion"]
population = response.json()[0]["population"]
currency = response.json()[0]["currencies"][0]["name"]
language = response.json()[0]["languages"][0]["name"]
countrycode = response.json()[0]["callingCodes"]
alpha3code = response.json()[0]["alpha3Code"]
area = response.json()[0]["area"]
timezones = response.json()[0]["timezones"]


linkweather = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weather_code&hourly=temperature_2m&current=temperature_2m&timezone=auto&start_date=2026-03-12&end_date=2026-03-13"

country = [name, latitude, longitude, capital, region, subregion, population, currency, language, countrycode, alpha3code, area, timezones]

for info in country:
  print(info)


weatherresponse = requests.get(linkweather)
weatherinfo = weatherresponse.json()
weathercode = weatherinfo["hourly"]["temperature_2m"]

for temperature in weathercode:
  print(temperature)

responsecountry = requests.get(linkcountry)

trip = input("Let's create a travel plan for your journey, please state your name: ")
tripcountries = input("Please state the countries you want to visit: ")
tripdates = int(input("Please state the total amount of days you will stay in this/those country/countries you want to visit: "))
if  tripdates > 1:
	print("Ok, let's continue")
else:
	print("That is not a valid answer")
notes = input("Are there any notes or special requirements you want to let us know?(answer yes or no): ")

if notes == "yes":
	input("Write them here: ")
elif notes == "no":
	print("Ok, let's continue")
else:
	print("That is not a valid answer")

countrieslist = tripcountries.split(",")
for tripcountries in countrieslist:
	tripcountries = tripcountries.strip()
	
priceAM = 30 #30$ a night
priceEU = 40 #40$ a night
priceAS = 25 #25$ a night
priceAF = 30 #30$ a night
priceOC = 35 #35$ a night

linkcountries = f"https://www.apicountries.com/name/{tripcountries}"

ans = requests.get(linkcountries)

region = ans.json()[0]["region"]

if tripcountries == country["region"]["Americas"]:
	print(f"That will be {tripdates * priceAM}$")
elif tripcountries == country["region"]["Europe"]:
	print(f"That will be {tripdates * priceEU}$")
elif tripcountries == country["region"]["Asia"]:
	print(f"That will be {tripdates * priceAS}$")
elif tripcountries == country["region"]["Africa"]:
	print(f"That will be {tripdates * priceAF}$")
elif tripcountries == country["region"]["Oceania"]:
	print(f"That will be {tripdates * priceOC}$")
else:
	print("That is not a valid country")

print(trip, tripcountries, tripdates, notes)

response = (responsecountry)

print(response.json()) 
