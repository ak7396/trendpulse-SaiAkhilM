# Import required libraries
import requests
import pandas as pd

# API endpoint with only required fields (optimized query)
url = "https://restcountries.com/v3.1/all?fields=name,capital,region,population,area"

# Initialize empty list (safe fallback if API fails)
data = []

try:
    # Send GET request to API
    response = requests.get(url)
    
    # Raise exception if status code is not 200
    response.raise_for_status()

    # Convert JSON response into Python object (list of dictionaries)
    data = response.json()

    # Print basic info
    print(f"Status Code: {response.status_code}")
    print(f"Total number of countries retrieved: {len(data)}")

except requests.exceptions.RequestException as e:
    # Handle all request-related errors
    print(f"Request failed: {e}")

# -------------------------------
# Step 2: Extract required fields
# -------------------------------

# Create empty list to store transformed data
rows = []

# Loop through each country (each element in list)
for country in data:
    
    # Extract nested and optional fields safely using .get()
    name = country.get("name", {}).get("common", "N/A")
    
    # Capital is a list → take first value, handle missing safely
    capital = (country.get("capital") or  ["N/A"])[0]
    
    region = country.get("region", "N/A")
    population = country.get("population", "N/A")

    area = country.get("area", 0)

    # Create a clean flattened dictionary
    row = {
        "country": name,
        "capital": capital,
        "region": region,
        "population": population,
        "area": area
    }

    # Append to list
    rows.append(row)
print(rows)
# -------------------------------
# Step 3: Convert to DataFrame
# -------------------------------

df = pd.DataFrame(rows)

# Display first few records
print("\nSample Data:")
print(df.head(100))

print("-----------------------------------------------------------------------------")

#Task 3 — Summarize the Data
#Which region has the highest total population?
#Which country has the largest area?
top_pop = df.sort_values("population", ascending=False).iloc[0]
print(f"Country with highest population: {top_pop['country']} ({top_pop['population']})")

top_area = df.sort_values("area", ascending=False).iloc[0]
print(f"Country with largest area: {top_area['country']} ({top_area['area']})")
