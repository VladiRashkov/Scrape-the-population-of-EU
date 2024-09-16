# Scrape-the-population-of-EU




# European Union Population Scraper
Description
This Python script scrapes population data for European Union member states from Wikipedia and stores it in a JSON file (countries_population.json). The script retrieves each country's population and percentage of the total EU population from the table on the provided Wikipedia page.

# Features
Scrapes the population and percentage data for EU countries.
Stores the data in a JSON file.
Updates the JSON file only when new or changed data is detected.

# Requirements
Python 3.x
requests library for handling HTTP requests
BeautifulSoup (bs4) for parsing HTML data
json for saving data in JSON format
os for file handling


You can install the required dependencies using git bash or the terminal with the following command:

pip install requests beautifulsoup4