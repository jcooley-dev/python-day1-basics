import pandas as pd

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

print("Downloading dataset...")

df = pd.read_csv(url)

print("\nDataset Preview:")
print(df.head())

europe = df[df["Region"] == "EUROPE"]

print("\nEuropean Countries:")
print(europe)

print("\nTotal European countries:", len(europe))

europe.to_csv("europe_countries.csv", index=False)
print("\nSaved europe_countries.csv")