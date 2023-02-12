brand = {
  "name": "Zara",
  "creation_date": 1975,
  "creator_name": "Amancio Ortega Gaona",
  "type_of_clothes": ["men", "women", "children", "home"],
  "international_competitors": ["Gap", "H&M", "Benetton"],
  "number_stores": 7000,
  "major_color": {
    "France": "blue",
    "Spain": "red",
    "US": ["pink", "green"]
  }
}

print("Brand name:", brand["name"])
print("Creation date:", brand["creation_date"])
print("Creator name:", brand["creator_name"])
print("Type of clothes:", brand["type_of_clothes"])
print("International competitors:", brand["international_competitors"])
print("Number of stores:", brand["number_stores"])
print("Major color:")
for key, value in brand["major_color"].items():
  print(f"  {key}: {value}")