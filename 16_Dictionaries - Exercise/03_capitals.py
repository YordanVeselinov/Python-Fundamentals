countries = input().split(", ")
capitals = input().split(", ")
zipping_countries_caputals = zip(countries, capitals)
my_dict = {key:value for key,value in zipping_countries_caputals}

for key,value in my_dict.items():
    print(f"{key} -> {value}")
