import json
import csv

def read_json(filename):
  with open(filename) as json_file:
    data = json.load(json_file)

  return data

def write_csv(filename, data):
  with open(filename, 'wb') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in data:
      writer.writerow(row)

def read_csv(filename):
  data = []
  with open(filename, 'rb') as csv_file:
    reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
      data.append(row)

  return data
