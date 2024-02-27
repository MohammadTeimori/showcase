import requests
from bs4 import BeautifulSoup
import csv
import re
from unidecode import unidecode  # Import the unidecode function

# Send a GET request to the URL
url = "https://nonstopkino.at/programm/?location=wien&weekday=all&time=all"
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the <a> tags with the class 'full-card-link'
tags = soup.find_all('a', class_='full-card-link')

# Specify the output path
output_path = "../output/movies.csv"

# Open a CSV file for writing
with open(output_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Movie Title", "Day", "Date", "Time"])  # Write the header

    # For each tag, extract the movie title, day, date, and time
    for tag in tags:
        title = unidecode(tag.find('h3').text)  # Convert the title to ASCII
        date_time = re.sub(r'(\D)(\d)', r'\1 \2', tag.find('div', class_='normal').text, 1).split()
        day = date_time[0] if len(date_time) > 0 else None
        date = date_time[1] if len(date_time) > 1 else None
        time = date_time[2] if len(date_time) > 2 else None
        writer.writerow([title, day, date, time])  # Write the data to the CSV file
