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
