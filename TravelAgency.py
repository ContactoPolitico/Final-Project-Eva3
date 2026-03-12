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


linkweather = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weather_code&hourly=temperature_2m&current=temperature_2m&timezone=auto&start_date=2026-03-11&end_date=2026-03-13"

country = [name, latitude, longitude, capital, region, subregion, population, currency, language]

for info in country:
  print(info)


weatherresponse = requests.get(linkweather)
weatherinfo = weatherresponse.json()
weathercode = weatherinfo["hourly"]["temperature_2m"]

for temperature in weathercode:
  print(temperature)