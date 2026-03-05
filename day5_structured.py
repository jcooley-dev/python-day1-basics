import requests 
import csv
from io import StringIO

def download_and_filter():
    url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

    response = requests.get(url)

    if response.status_code != 200:
        print("Download failed.")
        return
    
    print("Download successful.")

    with open("countries.csv", "w", encoding="utf-8", newline="") as f:
        f.write(response.text) 

    print("Saved as countries.csv")

    csv_data = StringIO(response.text, newline="")
    reader = csv.DictReader(csv_data)

    europe_count = 0

    for row in reader:
        if row["Region"] == "EUROPE":
             europe_count += 1


    print("Total European countries:", europe_count)

if __name__ == "__main__":
     download_and_filter()
