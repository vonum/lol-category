import csv

from player_stats_parser import format_player_stats

def write_data_to_csv():
  data = format_player_stats()
  with open('../formatted_data/player_stats.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in data:
      writer.writerow(row)

write_data_to_csv()
