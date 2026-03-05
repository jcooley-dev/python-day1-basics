import requests 
import csv
from io import StringIO

print("Day 6: Pulling CSV from the Web")

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

response = requests.get(url)

if response.status_code == 200:
    print("Successfully downloaded data.\n")

    with open("countries.csv", "w", encoding="utf-8", newline="") as f:
        f.write(response.text)

    print("Saved as countries.csv")

    csv_data = StringIO(response.text, newline="")
    reader = csv.DictReader(csv_data)

    europe_count = 0

    for row in reader:
        country = row["Country"]
        region = row["Region"]

        if region == "EUROPE":
            print(country, "-", region)
            europe_count += 1
    print("\nTotal European countries:", europe_count)

else:
    print("Failed to download data.")