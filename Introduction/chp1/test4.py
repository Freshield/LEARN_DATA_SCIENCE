import csv

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

print(mpg[:3])