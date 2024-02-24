centurie = int(input())
years = centurie * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60



print(f"{centurie} centuries = {years} years = {days} days = "
      f"{hours} hours = {minutes} minutes")