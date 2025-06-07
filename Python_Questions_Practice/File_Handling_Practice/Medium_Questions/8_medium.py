# Read a CSV file and convert it to a list of dictionaries (use  csv.DictReader).
import csv

filename = "Text files/data.csv"
data_list = []

with open(filename, "r") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        data_list.append(row)

print(data_list)