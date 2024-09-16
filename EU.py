import requests
from bs4 import BeautifulSoup
import json
import os

url = "https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})

countries = {}

for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    if len(columns) > 1:
        country = columns[0].text.strip()
        #!option if the data is collected from the table!
        population = int(columns[1].text.strip().replace(',', ''))
        percentage_population = float(columns[2].text.strip().replace('%',''))
        

        countries[country] = {
            'population': population,
            'percentage': percentage_population
        }


        #!option if we have to calculate the data anew and not from the wikitable, 
        # I will leave it in a comment!

            # countries[country] = population

            # sum the whole population
            # total_population = sum(countries.values())

            # # percent from the total population
            # for country in countries:
            #     countries[country] = {
            #         'population': countries[country],
            #         'percentage': (countries[country] / total_population) * 100
            #     }

json_file = 'countries_population.json'

if os.path.exists(json_file):
    with open(json_file, 'r') as jsfile:
        data = json.load(jsfile)
else:
    data = {}

if data != countries:
    with open(json_file, 'w') as file:
        json.dump(countries, file, indent=2)
    print("Updated and saved to file.")
else:
    print("No changes.")
