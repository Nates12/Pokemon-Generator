import requests
pokiName = input("Please enter a Pokemon name: ").lower()

req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokiName}")

if req.status_code == 200:
  reqs = req.json()
  name = reqs["name"].capitalize()
  
  abilities = []
  for ability in reqs["abilities"]:
  
      abilities.append(ability["ability"]["name"])
  print(f"Name: {name}")
  print(f"Abilities: {abilities}")
else:
  print("Pokemon not found. Please try again.")
  #exit()
