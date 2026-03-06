import pandas as pd

print("Day7: Pamdas -> GIS-ready CSV")

# Public CSV (cities w/ coordinates)
url = "https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv"

df = pd.read_csv(url)

print("\nColumns:")
print(df.columns)

print("\nPreview:")
print(df.head())

# --- Basic Cleaning ---
# Rename to clean GIS-friendly names
df = df.rename(columns={
    "City": "city",
    "State": "state",
    "Population": "population",
    "lat": "latitude",
    "lon": "longitude"
})

# Drop rows missing coordinates
df = df.dropna(subset=["latitude", "longitude"])

# Make sure types are correct
df["population"] = pd.to_numeric(df["population"], errors="coerce")
df = df.dropna(subset=["population"])

# Filters
# filter by state
fl = df[df["state"] == "Florida"].copy()

# filter by population threshold
big = df[df["population"] >= 200000].copy()

print(f"\nFlorida cities count: {len(fl)}")
print(f"Big cities (>=200k) count: {len(big)}")

# Export results (GIS-ready CSVs)
fl.to_csv("fl_cities.csv", index=False)
big.to_csv("big_cities_200k.csv", index=False)

print("\nSaved files:")
print(" - fl_cities.csv")
print(" - big_cities_200k.csv")